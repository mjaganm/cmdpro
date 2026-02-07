# CommandPro - Intelligent Command Line Error Helper

Two powerful versions for analyzing and fixing command errors:

## 🚀 Choose Your Path

### 🤖 **CommandPro ML** (NEW - AI-Powered)
Uses **Ollama** for intelligent, context-aware error analysis.

```powershell
# 10-minute setup with Ollama
ollama serve  # Terminal 1
ollama pull mistral  # Terminal 2
python ml_cli.py "your command"  # Terminal 3
```

**Best for:**
- Complex errors that need context
- Natural language understanding
- Professional-grade analysis
- Learning from error patterns

👉 **[Start: ML-QUICKSTART.md](ML-QUICKSTART.md)**

### ⚡ **CommandPro** (Original - Rule-Based)
Fast pattern matching with zero dependencies.

```powershell
python cli.py "command not found: xyz"
```

**Best for:**
- Quick instant analysis
- No setup needed
- Offline use
- Resource-constrained systems

👉 **[Start: GETTING-STARTED.md](GETTING-STARTED.md)**

## 📊 Feature Comparison

| Feature | CommandPro | CommandPro ML |
|---------|-----------|---------------|
| **Setup Time** | 1 min | 10 min |
| **Dependencies** | 0 | Ollama + 2 pip packages |
| **Analysis Speed** | Instant (<10ms) | 1-3 seconds |
| **Context Awareness** | Pattern-based | AI-powered |
| **Fallback** | N/A | Works without Ollama |
| **Privacy** | ✓ Fully local | ✓ Fully local |
| **Error Types** | 10 built-in | Unlimited (AI) |
| **Learning** | Fixed patterns | Context-aware |

## ✨ Key Features (Both Versions)

- **Intelligent Detection** - Identifies error types automatically
- **Actionable Solutions** - Step-by-step fix instructions
- **Real-World Examples** - Copy-paste command examples
- **100% Local Processing** - No external APIs, full privacy
- **PowerShell Integration** - Easy aliases and shortcuts
- **Hybrid Fallback** - ML version falls back to rule-based
- **Production-Ready** - Battle-tested, comprehensive

## 📖 Documentation
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