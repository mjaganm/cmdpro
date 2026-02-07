# CommandPro - Command Line Error Helper

A Python-based command line helper that intelligently analyzes error messages and provides actionable solutions. Perfect for Windows PowerShell, but works with any command line interface.

## 🚀 Quick Start

```powershell
# Analyze an error
python C:\src\cmdpro\cli.py "command not found: python3"

# Or interactive mode
python C:\src\cmdpro\cli.py
```

## ✨ Features

- **Intelligent Error Detection**: Identifies 10+ common error types
- **Practical Solutions**: Get step-by-step solutions for each error
- **Real-World Examples**: See how to fix issues with actual commands
- **Zero Dependencies**: Works with Python standard library only
- **Easy Integration**: PowerShell alias support for quick access
- **Interactive & CLI Modes**: Use inline or in interactive mode

## 📋 Supported Error Types

1. Command Not Found
2. File or Directory Not Found
3. Permission Denied
4. Port Already in Use
5. Module or Package Not Found
6. Network Connection Error
7. Authentication Failed
8. Syntax Error
9. Disk Space Error
10. Invalid Argument or Option

## 📖 Documentation

- [README-CMDPRO.md](README-CMDPRO.md) - Detailed usage and features
- [INSTALL.md](INSTALL.md) - Installation and setup guide
- [cmdpro.ps1](cmdpro.ps1) - PowerShell integration

## 🛠️ Files

```
cmdpro/
├── cli.py                    - Main CLI entry point
├── analyzer.py               - Error analysis engine
├── knowledge_base.py         - Error patterns & solutions database
├── config.py                 - Configuration settings
├── tests.py                  - Unit tests
├── test_analyzer.py          - Integration tests
├── cmdpro.ps1                - PowerShell integration script
├── setup.py                  - Package installation
├── README-CMDPRO.md          - Detailed documentation
└── INSTALL.md                - Installation guide
```

## 💻 Usage Examples

### Basic Usage
```powershell
python cli.py "ModuleNotFoundError: No module named 'requests'"
```

Output:
```
✓ Error Type: Module or Package Not Found

Suggested Solutions:
  1. Install the missing package: pip install <package-name>
  2. Check package name spelling.
  3. Ensure you're using the correct Python environment/virtual env.

Try These Examples:
  1. Install a package: pip install requests
  2. Install from requirements file: pip install -r requirements.txt
```

### PowerShell Integration
```powershell
# Add to PowerShell profile
& "C:\src\cmdpro\cmdpro.ps1"

# Then use anywhere
err "your error message"
```

## 🧪 Testing

Run all tests:
```powershell
python tests.py -v
```

Run integration tests:
```powershell
python test_analyzer.py
```

## 🔧 Adding Custom Errors

Edit `knowledge_base.py` and add your error patterns to `ERROR_PATTERNS` list. Each entry needs:
- `name`: Error type name
- `patterns`: List of regex patterns to match
- `solutions`: List of solution steps
- `examples`: List of example commands

## 📝 License

See [LICENSE](LICENSE) file

---

For more information, see [INSTALL.md](INSTALL.md) and [README-CMDPRO.md](README-CMDPRO.md)