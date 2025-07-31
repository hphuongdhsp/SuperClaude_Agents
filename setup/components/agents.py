"""
Agents component for SuperClaude agent installations
"""

import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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
            "category": "extensions",
        }

    def get_metadata_modifications(self) -> Dict[str, Any]:
        """Get metadata modifications for agents component"""
        return {
            "components": {
                "agents": {
                    "version": "1.0.0",
                    "installed": True,
                    "files_count": len(self.component_files),
                }
            },
            "agents": {
                "enabled": True,
                "version": "1.0.0",
                "auto_update": False,
                "installed_agents": self._get_installed_agent_names(),
            },
        }

    def _install(self, config: Dict[str, Any]) -> bool:
        """Install agents component"""
        self.logger.info("Installing SuperClaude agent collection...")

        # Ensure agents directory exists - install directly to ~/.claude/agents/
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
            # Preserve directory structure instead of flattening
            target_file = agents_dir / filename

            # Create subdirectories if needed
            target_file.parent.mkdir(parents=True, exist_ok=True)

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
            self.logger.warning(
                f"Installed {installed_count} agents with {failed_count} failures"
            )
        else:
            self.logger.success(f"Successfully installed {installed_count} agents")

        # Only proceed with post-install if we installed at least one agent
        if installed_count > 0:
            return self._post_install()
        else:
            return False

    def _post_install(self):
        """Post-installation tasks"""
        try:
            # Add component registration to metadata first
            self.settings_manager.add_component_registration(
                "agents",
                {
                    "version": "1.0.0",
                    "category": "extensions",
                    "files_count": len(self.component_files),
                    "installed_at": time.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3],
                },
            )
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
                # Use full path including subdirectories
                file_path = agents_dir / filename
                if self.file_manager.remove_file(file_path):
                    removed_count += 1
                    self.logger.debug(f"Removed {filename}")
                else:
                    self.logger.warning(f"Could not remove {filename}")

            # Remove agents directory if empty
            try:
                if agents_dir.exists():
                    remaining_files = list(agents_dir.glob("*"))
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

            self.logger.success(
                f"Agents component uninstalled ({removed_count} files removed)"
            )
            return True

        except Exception as e:
            self.logger.exception(f"Unexpected error during agents uninstallation: {e}")
            return False

    def get_dependencies(self) -> List[str]:
        """Get dependencies"""
        return []  # Agents can be installed independently

    def update(self, config: Dict[str, Any]) -> bool:
        """Update agents component"""
        try:
            self.logger.info("Updating SuperClaude agents component...")

            # Check current version
            current_version = self.settings_manager.get_component_version("agents")
            target_version = self.get_metadata()["version"]

            if current_version == target_version:
                self.logger.info(
                    f"Agents component already at version {target_version}"
                )
                return True

            self.logger.info(
                f"Updating agents component from {current_version} to {target_version}"
            )

            # Create backup of existing agent files
            agents_dir = self.install_dir / "agents"
            backup_files = []

            if agents_dir.exists():
                for filename in self.component_files:
                    # Use full path including subdirectories
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

                self.logger.success(
                    f"Agents component updated to version {target_version}"
                )
            else:
                # Restore from backup on failure
                self.logger.warning("Update failed, restoring from backup...")
                for backup_path in backup_files:
                    try:
                        original_path = backup_path.with_suffix("")
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
            # Use full path including subdirectories
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
                errors.append(
                    f"Version mismatch: installed {installed_version}, expected {expected_version}"
                )

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
        """Discover all agent files in subdirectories"""
        source_dir = self._get_source_dir()
        if not source_dir.exists():
            self.logger.warning(f"Agents source directory not found: {source_dir}")
            return []

        # Find all .md files in subdirectories of the agents directory
        agent_files = []
        for file_path in source_dir.rglob("*.md"):  # Use rglob for recursive search
            if file_path.is_file():
                # Skip README.md files
                if file_path.name.lower() == "readme.md":
                    continue
                # Store relative path from source_dir
                relative_path = file_path.relative_to(source_dir)
                agent_files.append(str(relative_path))

        self.logger.debug(f"Discovered {len(agent_files)} agent files")
        return sorted(agent_files)

    def _validate_agent_file(self, file_path: Path) -> bool:
        """Validate agent file has proper frontmatter"""
        try:
            content = file_path.read_text(encoding="utf-8")

            # Check for frontmatter
            if not content.startswith("---"):
                return False

            # Extract frontmatter
            match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
            if not match:
                return False

            # Parse YAML frontmatter
            frontmatter_text = match.group(1)

            try:
                if yaml:
                    # For complex multi-line descriptions, we need to handle YAML parsing errors
                    frontmatter = yaml.safe_load(frontmatter_text)
                else:
                    # Simple parsing fallback - enhanced to handle multi-line values better
                    frontmatter = {}
                    lines = frontmatter_text.strip().split("\n")
                    current_key = None
                    current_value = []

                    for line in lines:
                        # Check if this is a new key at the root level (no indentation)
                        if (
                            ":" in line
                            and not line.startswith(" ")
                            and not line.startswith("\t")
                        ):
                            # Special handling for fields that commonly appear in multi-line content
                            if any(
                                field in line
                                for field in ["tools:", "color:", "examples:"]
                            ):
                                # Save previous key-value pair
                                if current_key:
                                    value = "\n".join(current_value).strip()
                                    # Remove surrounding quotes if present
                                    if value.startswith('"') and value.endswith('"'):
                                        value = value[1:-1]
                                    elif value.startswith("'") and value.endswith("'"):
                                        value = value[1:-1]
                                    frontmatter[current_key] = value
                                # Start new key-value pair
                                key, value = line.split(":", 1)
                                current_key = key.strip()
                                current_value = [value.strip()] if value.strip() else []
                            # Check if line is actually a key (not part of multi-line content)
                            elif current_key and current_key == "description":
                                # This might be part of the description content
                                current_value.append(line)
                            else:
                                # Save previous key-value pair
                                if current_key:
                                    value = "\n".join(current_value).strip()
                                    # Remove surrounding quotes if present
                                    if value.startswith('"') and value.endswith('"'):
                                        value = value[1:-1]
                                    elif value.startswith("'") and value.endswith("'"):
                                        value = value[1:-1]
                                    frontmatter[current_key] = value
                                # Start new key-value pair
                                key, value = line.split(":", 1)
                                current_key = key.strip()
                                current_value = [value.strip()] if value.strip() else []
                        elif current_key:
                            # Continuation of multiline value
                            current_value.append(line)

                    # Save last key-value pair
                    if current_key:
                        value = "\n".join(current_value).strip()
                        # Remove surrounding quotes if present
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                        elif value.startswith("'") and value.endswith("'"):
                            value = value[1:-1]
                        frontmatter[current_key] = value
            except yaml.YAMLError as e:
                # If YAML parsing fails, try simple parsing to at least check required fields
                self.logger.debug(
                    f"YAML parsing failed for {file_path.name}, trying simple parsing: {e}"
                )
                frontmatter = {}
                # Simple regex-based parsing for basic fields
                name_match = re.search(
                    r"^name:\s*(.+)$", frontmatter_text, re.MULTILINE
                )
                desc_match = re.search(
                    r"^description:\s*(.+)", frontmatter_text, re.MULTILINE
                )

                if name_match:
                    frontmatter["name"] = name_match.group(1).strip()
                if desc_match:
                    # For description, capture everything until we hit another field or end
                    desc_start = desc_match.start()
                    # Find the next field (tools:, color:, etc.) or end of frontmatter
                    next_field = re.search(
                        r"^(tools|color|examples):",
                        frontmatter_text[desc_start:],
                        re.MULTILINE,
                    )
                    if next_field:
                        desc_end = desc_start + next_field.start()
                        frontmatter["description"] = frontmatter_text[
                            desc_start:desc_end
                        ].strip()
                    else:
                        frontmatter["description"] = frontmatter_text[
                            desc_start:
                        ].strip()
                    # Clean up the description
                    frontmatter["description"] = re.sub(
                        r"^description:\s*", "", frontmatter["description"]
                    )

            # Validate required fields
            required_fields = ["name", "description"]
            for field in required_fields:
                if field not in frontmatter:
                    self.logger.debug(
                        f"Agent {file_path.name} missing required field: {field}"
                    )
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
            for file_path in agents_dir.rglob("*.md"):  # Use rglob for recursive search
                try:
                    content = file_path.read_text(encoding="utf-8")
                    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
                    if match:
                        frontmatter_text = match.group(1)
                        try:
                            if yaml:
                                frontmatter = yaml.safe_load(frontmatter_text)
                            else:
                                # Use simple regex parsing as fallback
                                frontmatter = {}
                                name_match = re.search(
                                    r"^name:\s*(.+)$", frontmatter_text, re.MULTILINE
                                )
                                if name_match:
                                    frontmatter["name"] = name_match.group(1).strip()
                        except yaml.YAMLError:
                            # Use simple regex parsing for name field
                            frontmatter = {}
                            name_match = re.search(
                                r"^name:\s*(.+)$", frontmatter_text, re.MULTILINE
                            )
                            if name_match:
                                frontmatter["name"] = name_match.group(1).strip()

                        if "name" in frontmatter:
                            agent_names.append(frontmatter["name"])
                except Exception:
                    pass  # Skip invalid files

        return sorted(agent_names)

    def _display_agent_summary(self):
        """Display summary of installed agents"""
        agents_dir = self.install_dir / "agents"
        agents_info = []

        if agents_dir.exists():
            for file_path in sorted(
                agents_dir.rglob("*.md")
            ):  # Use rglob for recursive search
                try:
                    content = file_path.read_text(encoding="utf-8")
                    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
                    if match:
                        frontmatter_text = match.group(1)
                        try:
                            if yaml:
                                frontmatter = yaml.safe_load(frontmatter_text)
                            else:
                                # Use simple regex parsing as fallback
                                frontmatter = {}
                                name_match = re.search(
                                    r"^name:\s*(.+)$", frontmatter_text, re.MULTILINE
                                )
                                desc_match = re.search(
                                    r"^description:\s*(.+)",
                                    frontmatter_text,
                                    re.MULTILINE,
                                )
                                if name_match:
                                    frontmatter["name"] = name_match.group(1).strip()
                                if desc_match:
                                    # Get first line of description for summary
                                    frontmatter["description"] = desc_match.group(
                                        1
                                    ).strip()
                        except yaml.YAMLError:
                            # Use simple regex parsing for required fields
                            frontmatter = {}
                            name_match = re.search(
                                r"^name:\s*(.+)$", frontmatter_text, re.MULTILINE
                            )
                            desc_match = re.search(
                                r"^description:\s*(.+)", frontmatter_text, re.MULTILINE
                            )
                            if name_match:
                                frontmatter["name"] = name_match.group(1).strip()
                            if desc_match:
                                # Get first line of description for summary
                                frontmatter["description"] = desc_match.group(1).strip()

                        if "name" in frontmatter and "description" in frontmatter:
                            # Clean up description if it's multi-line - just get first meaningful part
                            desc = str(frontmatter["description"])
                            # If description starts with a quote, find the matching end quote
                            if desc.startswith('"') or desc.startswith("'"):
                                desc = desc[1:]
                                if desc.endswith('"') or desc.endswith("'"):
                                    desc = desc[:-1]
                            # Take first sentence or line
                            desc = desc.split("\n")[0].split(". ")[0]
                            agents_info.append(
                                {"name": frontmatter["name"], "description": desc}
                            )
                except Exception:
                    pass  # Skip invalid files

        if agents_info:
            self.logger.info("\n📊 Installed Agents Summary:")
            self.logger.info("=" * 80)

            # Display agents in alphabetical order
            for agent in sorted(agents_info, key=lambda x: x["name"]):
                self.logger.info(f"  • {agent['name']}: {agent['description'][:60]}...")

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
            "directory_structure": "Preserves source directory structure",
            "dependencies": self.get_dependencies(),
        }
