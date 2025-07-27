"""
Agents component for SuperClaude agent installations
"""

from typing import Dict, List, Tuple, Optional, Any
from pathlib import Path
import time
try:
    import yaml
except ImportError:
    # Use PyYAML if available, otherwise use simple parsing
    yaml = None
import re

from ..base.component import Component


class AgentsComponent(Component):
    """SuperClaude agents component for AI assistant configurations"""
    
    def __init__(self, install_dir: Optional[Path] = None):
        """Initialize agents component"""
        super().__init__(install_dir, Path("agents"))
    
    def get_metadata(self) -> Dict[str, str]:
        """Get component metadata"""
        return {
            "name": "agents",
            "version": "1.0.0",
            "description": "Claude Code agent collection for specialized AI behaviors",
            "category": "extensions"
        }
    
    def get_metadata_modifications(self) -> Dict[str, Any]:
        """Get metadata modifications for agents component"""
        return {
            "components": {
                "agents": {
                    "version": "1.0.0",
                    "installed": True,
                    "files_count": len(self.component_files)
                }
            },
            "agents": {
                "enabled": True,
                "version": "1.0.0",
                "auto_update": False,
                "installed_agents": self._get_installed_agent_names()
            }
        }
    
    def _install(self, config: Dict[str, Any]) -> bool:
        """Install agents component"""
        self.logger.info("Installing SuperClaude agent collection...")
        
        # Ensure agents directory exists
        agents_dir = self.install_dir / "agents"
        if not self.file_manager.ensure_directory(agents_dir):
            self.logger.error(f"Could not create agents directory: {agents_dir}")
            return False
        
        # Install agent files
        source_dir = self._get_source_dir()
        installed_count = 0
        failed_count = 0
        
        for filename in self.component_files:
            source_file = source_dir / filename
            target_file = agents_dir / filename
            
            try:
                # Validate agent frontmatter before copying
                if self._validate_agent_file(source_file):
                    if self.file_manager.copy_file(source_file, target_file):
                        installed_count += 1
                        self.logger.debug(f"Installed agent: {filename}")
                    else:
                        failed_count += 1
                        self.logger.error(f"Failed to install agent: {filename}")
                else:
                    failed_count += 1
                    self.logger.error(f"Invalid agent file format: {filename}")
            except Exception as e:
                failed_count += 1
                self.logger.error(f"Error installing agent {filename}: {e}")
        
        if failed_count > 0:
            self.logger.warning(f"Installed {installed_count} agents with {failed_count} failures")
        else:
            self.logger.success(f"Successfully installed {installed_count} agents")
        
        return installed_count > 0
    
    def _post_install(self):
        """Post-installation tasks"""
        try:
            # Add component registration to metadata first
            self.settings_manager.add_component_registration("agents", {
                "version": "1.0.0",
                "category": "extensions",
                "files_count": len(self.component_files),
                "installed_at": time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
            })
            self.logger.info("Updated metadata with agents component registration")
            
            # Update metadata with modifications
            metadata_mods = self.get_metadata_modifications()
            self.settings_manager.update_metadata(metadata_mods)
            self.logger.info("Updated metadata with agents configuration")
            
            # Display agent summary
            self._display_agent_summary()
            
        except Exception as e:
            self.logger.error(f"Failed to update metadata: {e}")
            return False

        return True
    
    def uninstall(self) -> bool:
        """Uninstall agents component"""
        try:
            self.logger.info("Uninstalling SuperClaude agents component...")
            
            # Remove agent files
            agents_dir = self.install_dir / "agents"
            removed_count = 0
            
            for filename in self.component_files:
                file_path = agents_dir / filename
                if self.file_manager.remove_file(file_path):
                    removed_count += 1
                    self.logger.debug(f"Removed {filename}")
                else:
                    self.logger.warning(f"Could not remove {filename}")
            
            # Remove agents directory if empty
            try:
                if agents_dir.exists():
                    remaining_files = list(agents_dir.iterdir())
                    if not remaining_files:
                        agents_dir.rmdir()
                        self.logger.debug("Removed empty agents directory")
            except Exception as e:
                self.logger.warning(f"Could not remove agents directory: {e}")
            
            # Update metadata to remove agents component
            try:
                if self.settings_manager.is_component_installed("agents"):
                    self.settings_manager.remove_component_registration("agents")
                    # Also remove agents configuration from metadata
                    metadata = self.settings_manager.load_metadata()
                    if "agents" in metadata:
                        del metadata["agents"]
                        self.settings_manager.save_metadata(metadata)
                    self.logger.info("Removed agents component from metadata")
            except Exception as e:
                self.logger.warning(f"Could not update metadata: {e}")
            
            self.logger.success(f"Agents component uninstalled ({removed_count} files removed)")
            return True
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during agents uninstallation: {e}")
            return False
    
    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return ["core"]  # Agents require core framework
    
    def update(self, config: Dict[str, Any]) -> bool:
        """Update agents component"""
        try:
            self.logger.info("Updating SuperClaude agents component...")
            
            # Check current version
            current_version = self.settings_manager.get_component_version("agents")
            target_version = self.get_metadata()["version"]
            
            if current_version == target_version:
                self.logger.info(f"Agents component already at version {target_version}")
                return True
            
            self.logger.info(f"Updating agents component from {current_version} to {target_version}")
            
            # Create backup of existing agent files
            agents_dir = self.install_dir / "agents"
            backup_files = []
            
            if agents_dir.exists():
                for filename in self.component_files:
                    file_path = agents_dir / filename
                    if file_path.exists():
                        backup_path = self.file_manager.backup_file(file_path)
                        if backup_path:
                            backup_files.append(backup_path)
                            self.logger.debug(f"Backed up {filename}")
            
            # Perform installation (overwrites existing files)
            success = self.install(config)
            
            if success:
                # Remove backup files on successful update
                for backup_path in backup_files:
                    try:
                        backup_path.unlink()
                    except Exception:
                        pass  # Ignore cleanup errors
                
                self.logger.success(f"Agents component updated to version {target_version}")
            else:
                # Restore from backup on failure
                self.logger.warning("Update failed, restoring from backup...")
                for backup_path in backup_files:
                    try:
                        original_path = backup_path.with_suffix('')
                        backup_path.rename(original_path)
                        self.logger.debug(f"Restored {original_path.name}")
                    except Exception as e:
                        self.logger.error(f"Could not restore {backup_path}: {e}")
            
            return success
            
        except Exception as e:
            self.logger.exception(f"Unexpected error during agents update: {e}")
            return False
    
    def validate_installation(self) -> Tuple[bool, List[str]]:
        """Validate agents component installation"""
        errors = []
        
        # Check if agents directory exists
        agents_dir = self.install_dir / "agents"
        if not agents_dir.exists():
            errors.append("Agents directory not found")
            return False, errors
        
        # Check if all agent files exist and are valid
        valid_agents = 0
        for filename in self.component_files:
            file_path = agents_dir / filename
            if not file_path.exists():
                errors.append(f"Missing agent file: {filename}")
            elif not file_path.is_file():
                errors.append(f"Agent file is not a regular file: {filename}")
            else:
                # Validate agent file format
                if self._validate_agent_file(file_path):
                    valid_agents += 1
                else:
                    errors.append(f"Invalid agent file format: {filename}")
        
        # Check metadata registration
        if not self.settings_manager.is_component_installed("agents"):
            errors.append("Agents component not registered in metadata")
        else:
            # Check version matches
            installed_version = self.settings_manager.get_component_version("agents")
            expected_version = self.get_metadata()["version"]
            if installed_version != expected_version:
                errors.append(f"Version mismatch: installed {installed_version}, expected {expected_version}")
        
        # Log summary
        if valid_agents > 0:
            self.logger.info(f"Found {valid_agents} valid agents installed")
        
        return len(errors) == 0, errors
    
    def _get_source_dir(self) -> Path:
        """Get source directory for agent files"""
        # Assume we're in SuperClaude/setup/components/agents.py
        # and agent files are in SuperClaude/SuperClaude/Agents/
        project_root = Path(__file__).parent.parent.parent
        return project_root / "SuperClaude" / "Agents"
    
    def _discover_component_files(self) -> List[str]:
        """Discover all agent files"""
        source_dir = self._get_source_dir()
        if not source_dir.exists():
            self.logger.warning(f"Agents source directory not found: {source_dir}")
            return []
        
        # Find all .md files in the agents directory
        agent_files = []
        for file_path in source_dir.glob("*.md"):
            if file_path.is_file():
                agent_files.append(file_path.name)
        
        self.logger.debug(f"Discovered {len(agent_files)} agent files")
        return sorted(agent_files)
    
    def _validate_agent_file(self, file_path: Path) -> bool:
        """Validate agent file has proper frontmatter"""
        try:
            content = file_path.read_text(encoding='utf-8')
            
            # Check for frontmatter
            if not content.startswith('---'):
                return False
            
            # Extract frontmatter
            match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
            if not match:
                return False
            
            # Parse YAML frontmatter
            frontmatter_text = match.group(1)
            
            if yaml:
                frontmatter = yaml.safe_load(frontmatter_text)
            else:
                # Simple parsing fallback
                frontmatter = {}
                lines = frontmatter_text.strip().split('\n')
                current_key = None
                current_value = []
                
                for line in lines:
                    if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
                        # Save previous key-value pair
                        if current_key:
                            frontmatter[current_key] = ' '.join(current_value).strip().strip('"\'')
                        # Start new key-value pair
                        key, value = line.split(':', 1)
                        current_key = key.strip()
                        current_value = [value.strip()]
                    elif current_key:
                        # Continuation of multiline value
                        current_value.append(line.strip())
                
                # Save last key-value pair
                if current_key:
                    frontmatter[current_key] = ' '.join(current_value).strip().strip('"\'')
            
            # Validate required fields
            required_fields = ['name', 'description']
            for field in required_fields:
                if field not in frontmatter:
                    self.logger.debug(f"Agent {file_path.name} missing required field: {field}")
                    return False
            
            return True
            
        except Exception as e:
            self.logger.debug(f"Error validating agent file {file_path.name}: {e}")
            return False
    
    def _get_installed_agent_names(self) -> List[str]:
        """Get list of installed agent names"""
        agents_dir = self.install_dir / "agents"
        agent_names = []
        
        if agents_dir.exists():
            for file_path in agents_dir.glob("*.md"):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if match:
                        frontmatter_text = match.group(1)
                        if yaml:
                            frontmatter = yaml.safe_load(frontmatter_text)
                        else:
                            # Simple parsing fallback
                            frontmatter = {}
                            lines = frontmatter_text.strip().split('\n')
                            current_key = None
                            current_value = []
                            
                            for line in lines:
                                if ':' in line and not line.startswith(' ') and not line.startswith('\t'):
                                    # Save previous key-value pair
                                    if current_key:
                                        frontmatter[current_key] = ' '.join(current_value).strip().strip('"\'')
                                    # Start new key-value pair
                                    key, value = line.split(':', 1)
                                    current_key = key.strip()
                                    current_value = [value.strip()]
                                elif current_key:
                                    # Continuation of multiline value
                                    current_value.append(line.strip())
                            
                            # Save last key-value pair
                            if current_key:
                                frontmatter[current_key] = ' '.join(current_value).strip().strip('"\'')
                        if 'name' in frontmatter:
                            agent_names.append(frontmatter['name'])
                except Exception:
                    pass  # Skip invalid files
        
        return sorted(agent_names)
    
    def _display_agent_summary(self):
        """Display summary of installed agents"""
        agents_dir = self.install_dir / "agents"
        agents_info = []
        
        if agents_dir.exists():
            for file_path in sorted(agents_dir.glob("*.md")):
                try:
                    content = file_path.read_text(encoding='utf-8')
                    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
                    if match:
                        frontmatter_text = match.group(1)
                        if yaml:
                            frontmatter = yaml.safe_load(frontmatter_text)
                        else:
                            # Simple parsing fallback
                            frontmatter = {}
                            for line in frontmatter_text.split('\n'):
                                if ':' in line:
                                    key, value = line.split(':', 1)
                                    frontmatter[key.strip()] = value.strip().strip('"\'')
                        if 'name' in frontmatter and 'description' in frontmatter:
                            agents_info.append({
                                'name': frontmatter['name'],
                                'description': frontmatter['description']
                            })
                except Exception:
                    pass  # Skip invalid files
        
        if agents_info:
            self.logger.info("\n📊 Installed Agents Summary:")
            self.logger.info("=" * 80)
            for agent in agents_info:
                self.logger.info(f"• {agent['name']}: {agent['description'][:60]}...")
            self.logger.info("=" * 80)
            self.logger.info(f"Total agents installed: {len(agents_info)}")
    
    def get_size_estimate(self) -> int:
        """Get estimated installation size"""
        total_size = 0
        source_dir = self._get_source_dir()
        
        for filename in self.component_files:
            file_path = source_dir / filename
            if file_path.exists():
                total_size += file_path.stat().st_size
        
        # Add overhead for directory and settings
        total_size += 2048  # ~2KB overhead
        
        return total_size
    
    def get_installation_summary(self) -> Dict[str, Any]:
        """Get installation summary"""
        return {
            "component": self.get_metadata()["name"],
            "version": self.get_metadata()["version"],
            "files_installed": len(self.component_files),
            "agent_files": self.component_files,
            "estimated_size": self.get_size_estimate(),
            "install_directory": str(self.install_dir / "agents"),
            "dependencies": self.get_dependencies()
        }