# SuperClaude v3 🚀 (Forked)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-3.0.0--fork-blue.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents)
[![GitHub issues](https://img.shields.io/github/issues/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/issues)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/CONTRIBUTING.md)
[![Contributors](https://img.shields.io/github/contributors/hphuongdhsp/SuperClaude_Agents)](https://github.com/hphuongdhsp/SuperClaude_Agents/graphs/contributors)

Một framework mở rộng Claude Code với các lệnh chuyên biệt, personas và tích hợp MCP server.

**📢 Trạng thái**: Đây là một fork của dự án SuperClaude v3 gốc. Fork này nhằm tiếp tục phát triển và cung cấp cài đặt từ mã nguồn.

## SuperClaude là gì? 🤔

SuperClaude cố gắng làm cho Claude Code hữu ích hơn cho công việc phát triển bằng cách thêm:
- 🛠️ **16 lệnh chuyên biệt** cho các tác vụ phát triển thường gặp (một số hoạt động tốt hơn những cái khác!)
- 🤖 **35 AI agents** với chuyên môn đặc biệt (đánh giá mã, kiến trúc, testing, v.v.)
- 🎭 **Smart personas** thường chọn đúng chuyên gia cho các lĩnh vực khác nhau
- 🔧 **Tích hợp MCP server** cho tài liệu, UI components và tự động hóa trình duyệt
- 📋 **Quản lý tác vụ** cố gắng theo dõi tiến trình
- ⚡ **Tối ưu hóa token** để giúp với các cuộc trò chuyện dài hơn

Đây là điều chúng tôi đã xây dựng để làm cho quy trình phát triển mượt mà hơn. Vẫn còn thô ráp, nhưng đang ngày càng tốt hơn! 😊

## Trạng thái hiện tại 📊

✅ **Những gì hoạt động tốt:**
- Bộ cài đặt (được viết lại từ đầu)
- Framework cốt lõi với 9 tệp tài liệu
- 16 slash commands cho các tác vụ phát triển khác nhau
- 35 AI agents chuyên biệt để hỗ trợ theo lĩnh vực
- Tích hợp MCP server (Context7, Sequential, Magic, Playwright)
- Trình cài đặt CLI thống nhất để thiết lập dễ dàng

⚠️ **Các vấn đề đã biết:**
- Đây là phiên bản phát hành đầu tiên - bugs là điều được mong đợi
- Một số tính năng có thể chưa hoạt động hoàn hảo
- Tài liệu vẫn đang được cải thiện
- Hệ thống Hooks đã được gỡ bỏ (sẽ trở lại trong v4)

## Tính năng chính ✨

### Lệnh 🛠️
Chúng tôi tập trung vào 16 lệnh thiết yếu cho các tác vụ phổ biến nhất:

**Phát triển**: `/sc:implement`, `/sc:build`, `/sc:design`  
**Phân tích**: `/sc:analyze`, `/sc:troubleshoot`, `/sc:explain`  
**Chất lượng**: `/sc:improve`, `/sc:test`, `/sc:cleanup`  
**Khác**: `/sc:document`, `/sc:git`, `/sc:estimate`, `/sc:task`, `/sc:index`, `/sc:load`, `/sc:spawn`

### Smart Personas 🎭
Các chuyên gia AI cố gắng tham gia khi chúng có vẻ phù hợp:
- 🏗️ **architect** - Thiết kế hệ thống và kiến trúc
- 🎨 **frontend** - UI/UX và khả năng tiếp cận
- ⚙️ **backend** - APIs và cơ sở hạ tầng
- 🔍 **analyzer** - Debug và tìm hiểu vấn đề
- 🛡️ **security** - Mối quan tâm về bảo mật và lỗ hổng
- ✍️ **scribe** - Tài liệu và viết
- *...và 5 chuyên gia khác*

*(Chúng không phải lúc nào cũng chọn hoàn hảo, nhưng thường đúng!)*

### AI Agents 🤖
35 agents chuyên biệt cho các tác vụ và lĩnh vực cụ thể:
- **Phát triển**: `ai-engineer`, `backend-architect`, `frontend-developer`, `golang-pro`, `python-pro`
- **Chất lượng mã**: `code-reviewer`, `code-refactorer`, `debugger`, `test-automator`
- **Cơ sở hạ tầng**: `cloud-architect`, `deployment-engineer`, `devops-troubleshooter`
- **Chuyên biệt**: `data-scientist`, `ml-engineer`, `security-auditor`, `performance-engineer`
- **Tài liệu**: `api-documenter`, `content-writer`, `prompt-engineer`

Mỗi agent có chuyên môn độc đáo, sở thích công cụ và cách tiếp cận. Xem [Docs/agents-guide.md](Docs/agents-guide.md) để biết chi tiết.

### Tích hợp MCP 🔧
Các công cụ bên ngoài kết nối khi hữu ích:
- **Context7** - Lấy tài liệu thư viện chính thức và patterns
- **Sequential** - Giúp với tư duy phức tạp nhiều bước
- **Magic** - Tạo UI components hiện đại
- **Playwright** - Tự động hóa trình duyệt và testing

*(Những cái này hoạt động khá tốt khi chúng kết nối đúng cách! 🤞)*

## ⚠️ Nâng cấp từ v2? Quan trọng!

Nếu bạn đang đến từ SuperClaude v2, bạn cần dọn dẹp trước:

1. **Gỡ cài đặt v2** sử dụng trình gỡ cài đặt nếu có
2. **Dọn dẹp thủ công** - xóa những cái này nếu chúng tồn tại:
   - `SuperClaude/`
   - `~/.claude/shared/`
   - `~/.claude/commands/`
   - `~/.claude/CLAUDE.md`
3. **Sau đó tiến hành** với cài đặt v3 bên dưới

Điều này là do v3 có cấu trúc khác và các tệp cũ có thể gây xung đột.

### 🔄 **Thay đổi chính cho người dùng v2**
**Lệnh `/build` đã thay đổi!** Trong v2, `/build` được sử dụng để triển khai tính năng. Trong v3:
- `/sc:build` = chỉ biên dịch/đóng gói
- `/sc:implement` = triển khai tính năng (MỚI!)

**Di chuyển**: Thay thế `v2 /build myFeature` bằng `v3 /sc:implement myFeature`

## Cài đặt 📦

Cài đặt SuperClaude là một **quy trình hai bước**:
1. Đầu tiên cài đặt Python package
2. Sau đó chạy trình cài đặt để thiết lập tích hợp Claude Code

Chọn hệ điều hành của bạn bên dưới để có hướng dẫn chi tiết từng bước:

## 🍎 Cài đặt cho người dùng Mac

### Điều kiện tiên quyết
Đầu tiên, hãy đảm bảo bạn có mọi thứ cần thiết:

**Bước 1: Cài đặt Homebrew (nếu bạn chưa có)**
1. Mở Terminal (nhấn `Cmd + Space`, gõ "Terminal", và nhấn Enter)
2. Sao chép và dán lệnh này:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Nhấn Enter và làm theo hướng dẫn
4. Khi hoàn thành, khởi động lại Terminal

**Bước 2: Cài đặt Python 3**
1. Trong Terminal, chạy:
   ```bash
   brew install python3
   ```
2. Xác minh Python đã được cài đặt:
   ```bash
   python3 --version
   ```
   Bạn sẽ thấy cái gì đó như "Python 3.11.x" hoặc cao hơn

**Bước 3: Cài đặt Git (nếu bạn chưa có)**
```bash
brew install git
```

### Quy trình cài đặt

**Bước 4: Tải xuống SuperClaude**
1. Trong Terminal, điều hướng đến nơi bạn muốn cài đặt SuperClaude (ví dụ: thư mục home của bạn):
   ```bash
   cd ~
   ```
2. Clone repository:
   ```bash
   git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
   ```
3. Vào thư mục SuperClaude:
   ```bash
   cd SuperClaude_Agents
   ```

**Bước 5: Cài đặt UV (trình quản lý package được khuyến nghị)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Sau đó khởi động lại terminal của bạn hoặc chạy:
```bash
source ~/.bashrc
```

**Bước 6: Cài đặt SuperClaude**
```bash
uv sync
```

**Bước 7: Chạy trình cài đặt SuperClaude**
```bash
python3 -m SuperClaude install
```

**Xong! 🎉** SuperClaude giờ đã được cài đặt và sẵn sàng sử dụng với Claude Code.

---

## 🐧 Cài đặt cho người dùng Ubuntu

### Điều kiện tiên quyết
Đầu tiên, hãy đảm bảo hệ thống của bạn được cập nhật và có mọi thứ cần thiết:

**Bước 1: Cập nhật hệ thống của bạn**
1. Mở Terminal (nhấn `Ctrl + Alt + T`)
2. Cập nhật danh sách package:
   ```bash
   sudo apt update
   ```
3. Nâng cấp các package đã cài đặt:
   ```bash
   sudo apt upgrade -y
   ```

**Bước 2: Cài đặt Python 3 và pip**
```bash
sudo apt install python3 python3-pip python3-venv git curl -y
```

**Bước 3: Xác minh cài đặt Python**
```bash
python3 --version
```
Bạn sẽ thấy cái gì đó như "Python 3.8.x" hoặc cao hơn

### Quy trình cài đặt

**Bước 4: Tải xuống SuperClaude**
1. Điều hướng đến thư mục home của bạn:
   ```bash
   cd ~
   ```
2. Clone repository:
   ```bash
   git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
   ```
3. Vào thư mục SuperClaude:
   ```bash
   cd SuperClaude_Agents
   ```

**Bước 5: Cài đặt UV (trình quản lý package được khuyến nghị)**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
Sau đó tải lại cấu hình shell của bạn:
```bash
source ~/.bashrc
```
Hoặc khởi động lại terminal của bạn.

**Bước 6: Cài đặt SuperClaude**
```bash
uv sync
```

**Bước 7: Chạy trình cài đặt SuperClaude**
```bash
python3 -m SuperClaude install
```

**Xong! 🎉** SuperClaude giờ đã được cài đặt và sẵn sàng sử dụng với Claude Code.

---

## 🔄 Phương pháp cài đặt thay thế

### Sử dụng UV (Người dùng nâng cao)
Nếu bạn thích sử dụng `uv` trực tiếp để có hiệu suất tốt hơn:

```bash
# Sau khi clone repository:
cd SuperClaude_Agents
uv venv
source .venv/bin/activate  # Trên Mac/Linux
uv sync
```

### Sử dụng UVX (Đa nền tảng)
```bash
git clone https://github.com/hphuongdhsp/SuperClaude_Agents.git
cd SuperClaude_Agents
uvx run uv sync
```

---

## 📋 Xác minh cài đặt

Sau khi cài đặt, xác minh mọi thứ hoạt động:

1. **Kiểm tra xem SuperClaude đã được cài đặt:**
   ```bash
   python3 -m SuperClaude --help
   ```

2. **Thử một lệnh cơ bản:**
   ```bash
   SuperClaude install --help
   ```

Nếu bạn thấy thông tin trợ giúp, chúc mừng! SuperClaude đã được cài đặt đúng cách.

---

## 🚨 Khắc phục các vấn đề phổ biến

**Vấn đề: "command not found: python3"**
- **Mac**: Cài đặt Python với `brew install python3`
- **Ubuntu**: Cài đặt với `sudo apt install python3`

**Vấn đề: "command not found: git"**
- **Mac**: Cài đặt với `brew install git`
- **Ubuntu**: Cài đặt với `sudo apt install git`

**Vấn đề: Lỗi "Permission denied"**
- Không bao giờ sử dụng `sudo` với cài đặt SuperClaude
- Đảm bảo bạn cài đặt trong thư mục home của mình

**Vấn đề: "uv: command not found"**
- Script cài đặt uv có thể cần bạn khởi động lại terminal
- Hoặc thủ công source cấu hình shell của bạn: `source ~/.bashrc`

**Cần thêm trợ giúp?** Mở một issue trên [trang GitHub](https://github.com/hphuongdhsp/SuperClaude_Agents/issues) của chúng tôi.

## ⚙️ Tùy chọn trình cài đặt

Sau khi làm theo các bước cài đặt theo nền tảng ở trên, bạn có thể tùy chỉnh cài đặt SuperClaude của mình với các tùy chọn này:

### Profiles cài đặt

**Thiết lập nhanh (Được khuyến nghị cho hầu hết người dùng)**
```bash
python3 -m SuperClaude install
```

**Lựa chọn tương tác (Chọn components)**
```bash
python3 -m SuperClaude install --interactive
```

**Cài đặt tối thiểu (Chỉ framework cốt lõi)**
```bash
python3 -m SuperClaude install --minimal
```

**Thiết lập Developer (Bao gồm mọi thứ)**
```bash
python3 -m SuperClaude install --profile developer
```

### Định dạng lệnh thay thế

Bạn cũng có thể sử dụng các định dạng tương đương này:

**Kiểu Python Module:**
```bash
python3 -m SuperClaude install [options]
```

**Thực thi Python trực tiếp:**
```bash
python3 SuperClaude install [options]
```

**Lệnh Bash đơn giản (nếu có trong PATH):**
```bash
SuperClaude install [options]
```

### Nhận trợ giúp
```bash
python3 -m SuperClaude install --help
```

**Xong! 🎉** Trình cài đặt xử lý mọi thứ: framework files, MCP servers và cấu hình Claude Code.

## Cách hoạt động 🔄

SuperClaude cố gắng nâng cao Claude Code thông qua:

1. **Framework Files** - Tài liệu được cài đặt vào `~/.claude/` hướng dẫn cách Claude phản hồi
2. **Slash Commands** - 16 lệnh chuyên biệt cho các tác vụ phát triển khác nhau
3. **MCP Servers** - Các dịch vụ bên ngoài thêm khả năng bổ sung (khi chúng hoạt động!)
4. **Smart Routing** - Cố gắng chọn đúng công cụ và chuyên gia dựa trên những gì bạn đang làm

Hầu hết thời gian nó hoạt động tốt với những thứ hiện có của Claude Code. 🤝

## Sắp tới trong v4 🔮

Chúng tôi hy vọng sẽ làm việc trên những điều này cho phiên bản tiếp theo:
- **Hooks System** - Những thứ event-driven (đã gỡ bỏ khỏi v3, đang cố gắng thiết kế lại đúng cách)
- **MCP Suite** - Nhiều tích hợp công cụ bên ngoài hơn
- **Hiệu suất tốt hơn** - Cố gắng làm cho mọi thứ nhanh hơn và ít lỗi hơn
- **Nhiều Personas hơn** - Có thể một vài chuyên gia lĩnh vực nữa
- **Hỗ trợ Cross-CLI** - Có thể hoạt động với các trợ lý coding AI khác

*(Không có lời hứa về timeline - chúng tôi vẫn đang tìm hiểu v3! 😅)*

## Thêm lệnh tùy chỉnh 🛠️

### Bắt đầu nhanh
Bạn có thể mở rộng SuperClaude với các slash commands tùy chỉnh của riêng mình! Đây là cách:

1. **Tạo một file markdown** trong `SuperClaude/Commands/custom/`
2. **Thêm metadata bắt buộc** (YAML frontmatter)
3. **Chạy** `SuperClaude install` để đăng ký

Ví dụ lệnh tùy chỉnh:
```markdown
---
allowed-tools: [Read, Grep, Glob]
description: "Phân tích và tóm tắt nội dung thư mục"
---

# /sc:mysummary - Custom Folder Analyzer

## Mục đích
Cung cấp insights về cấu trúc và nội dung thư mục.

## Sử dụng
```
/sc:mysummary @folder
```
```

Xong! Lệnh của bạn giờ đã có sẵn trong Claude Code.

📚 **Để có hướng dẫn chi tiết**, xem:
- [Custom Commands Developer Guide](Docs/custom-commands-guide.md)
- [Command Format Specification](Docs/command-format-specification.md)

## Cấu hình ⚙️

Sau khi cài đặt, bạn có thể tùy chỉnh SuperClaude bằng cách chỉnh sửa:
- `~/.claude/settings.json` - Cấu hình chính
- `~/.claude/*.md` - Framework behavior files

Hầu hết người dùng có thể không cần thay đổi gì - nó thường hoạt động ổn ngay từ đầu. 🎛️

## Tài liệu 📖

Muốn tìm hiểu thêm? Xem các hướng dẫn của chúng tôi:

- 📚 [**User Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/superclaude-user-guide.md) - Tổng quan hoàn chỉnh và bắt đầu
- 🛠️ [**Commands Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/commands-guide.md) - Tất cả 16 slash commands được giải thích
- 🏳️ [**Flags Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/flags-guide.md) - Command flags và options
- 🎭 [**Personas Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/personas-guide.md) - Hiểu hệ thống persona
- 📦 [**Installation Guide**](https://github.com/hphuongdhsp/SuperClaude_Agents/blob/master/Docs/installation-guide.md) - Hướng dẫn cài đặt chi tiết

Các hướng dẫn này có nhiều chi tiết hơn README này và được cập nhật thường xuyên.

## Đóng góp 🤝

Chúng tôi chào đón sự đóng góp! Các lĩnh vực mà chúng tôi có thể cần trợ giúp:
- 🐛 **Bug Reports** - Cho chúng tôi biết điều gì bị hỏng
- 📝 **Documentation** - Giúp chúng tôi giải thích mọi thứ tốt hơn
- 🧪 **Testing** - Nhiều test coverage hơn cho các thiết lập khác nhau
- 💡 **Ideas** - Đề xuất cho các tính năng hoặc cải tiến mới

Codebase là Python khá đơn giản + các tệp tài liệu.

## Cấu trúc dự án 📁

```
SuperClaude/
├── setup.py               # pypi setup file
├── SuperClaude/           # Framework files  
│   ├── Core/              # Behavior documentation (COMMANDS.md, FLAGS.md, etc.)
│   ├── Commands/          # 16 slash command definitions
│   └── Settings/          # Configuration files
├── setup/                 # Installation system
└── profiles/              # Installation profiles (quick, minimal, developer)
```

## Ghi chú kiến trúc 🏗️

Kiến trúc v3 tập trung vào:
- **Đơn giản** - Gỡ bỏ sự phức tạp không thêm giá trị
- **Độ tin cậy** - Cài đặt tốt hơn và ít thay đổi gây hỏng hơn
- **Tính modular** - Chỉ chọn các components bạn muốn
- **Hiệu suất** - Hoạt động nhanh hơn với caching thông minh hơn

## Giấy phép

MIT - [Xem file LICENSE để biết chi tiết](https://opensource.org/licenses/MIT)

## Lịch sử Star

<a href="https://www.star-history.com/#hphuongdhsp/SuperClaude_Agents&Date">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date&theme=dark" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date" />
   <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=hphuongdhsp/SuperClaude_Agents&type=Date" />
 </picture>
</a>

---

*Được xây dựng bởi các developers mệt mỏi với các phản hồi chung chung. Hy vọng bạn thấy nó hữu ích! 🙂*

---