# CommandPro - Getting Started

Welcome to CommandPro! This guide will help you get up and running in 5 minutes.

## 🚀 5-Minute Setup

### Step 1: Verify Python Installation
```powershell
python --version
```
You need Python 3.7 or later. If not installed, download from https://www.python.org/

### Step 2: Navigate to CommandPro
```powershell
cd C:\src\cmdpro
```

### Step 3: Test It Works
```powershell
python cli.py "command not found: xyz"
```

You should see:
```
✓ Error Type: Command Not Found

Suggested Solutions:
  1. The command may not be installed. Check if it's in your PATH.
  2. Try installing the missing tool using package managers (pip, choco, etc.)
  3. Verify the command name is spelled correctly.
```

## 💻 How to Use

### Method 1: Direct CLI (Quickest)
```powershell
python C:\src\cmdpro\cli.py "your error message here"
```

### Method 2: Interactive Mode (Easiest)
```powershell
python C:\src\cmdpro\cli.py
# Paste your error message
# Press Enter twice to analyze
```

### Method 3: PowerShell Alias (Most Convenient)

Add this to your PowerShell profile:
```powershell
# Edit your profile
notepad $PROFILE

# Add this line to the file
& "C:\src\cmdpro\cmdpro.ps1"
```

Then restart PowerShell and use:
```powershell
err "your error message"
```

## 🎯 Try These Examples

```powershell
# Example 1: Package not found
python cli.py "ModuleNotFoundError: No module named requests"

# Example 2: File not found
python cli.py "cannot find the path specified"

# Example 3: Permission error
python cli.py "Access is denied"

# Example 4: Port in use
python cli.py "Address already in use: port 8000"

# Example 5: Syntax error
python cli.py "SyntaxError: unexpected token"
```

## 🔍 What Errors Can It Identify?

CommandPro understands 10 common error types:

1. **Command Not Found** - "command not found", "not recognized as a cmdlet"
2. **File Not Found** - "cannot find the path", "No such file"
3. **Permission Issues** - "Access is denied", "Permission denied"
4. **Port Issues** - "Address already in use"
5. **Missing Packages** - "ModuleNotFoundError", "No module named"
6. **Network Issues** - "Connection timeout", "Connection refused"
7. **Auth Issues** - "authentication failed", "401 Unauthorized"
8. **Syntax Issues** - "SyntaxError", "unexpected token"
9. **Disk Issues** - "no space left on device", "disk full"
10. **Argument Issues** - "unrecognized arguments", "invalid argument"

## 📚 Documentation

For more information:
- **Quick reference**: Open `QUICK-REFERENCE.md`
- **Detailed guide**: Open `README-CMDPRO.md`
- **Installation help**: Open `INSTALL.md`
- **Code examples**: Run `python examples.py`

## 🧪 Test It

Run the automated tests:
```powershell
python tests.py -v
```

## 🎓 Learn More

### See It in Action
```powershell
python test_analyzer.py
```
This shows CommandPro analyzing 10 different error types.

### Explore the Code
- `cli.py` - User interface
- `analyzer.py` - Analysis engine
- `knowledge_base.py` - Error patterns and solutions

### Review Examples
```powershell
python examples.py
```

## ❓ Frequently Asked Questions

**Q: Do I need to install anything?**
A: No! CommandPro uses only Python's standard library. Just have Python 3.7+ installed.

**Q: Can I add custom errors?**
A: Yes! Edit `knowledge_base.py` and add your error patterns to `ERROR_PATTERNS`.

**Q: How do I set up the PowerShell alias?**
A: Run:
```powershell
& "C:\src\cmdpro\cmdpro.ps1"
```
Then edit your profile at `$PROFILE` to make it permanent.

**Q: What if my error isn't recognized?**
A: CommandPro will still provide general suggestions. You can add your error pattern to `knowledge_base.py`.

**Q: Can I use this in my Python code?**
A: Absolutely! Import and use the ErrorAnalyzer class:
```python
from analyzer import ErrorAnalyzer
result = ErrorAnalyzer.analyze("error message")
print(result['solutions'])
```

## 🚨 Troubleshooting

| Problem | Solution |
|---|---|
| `ModuleNotFoundError` | Make sure you're in `C:\src\cmdpro` directory |
| `python: command not found` | Install Python or add to PATH |
| PowerShell profile issues | Run: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Tests failing | Make sure Python version is 3.7+ |

## ✨ Next Steps

1. **Try the examples above**
2. **Set up the PowerShell alias for easy access**
3. **Explore the code in `knowledge_base.py`**
4. **Run the test suite to see what's supported**
5. **Add your own error patterns**

## 📞 Need Help?

- Check the error message - it might suggest a fix!
- Read the detailed docs: `README-CMDPRO.md`
- Look at examples: `python examples.py`
- Check your Python version: `python --version`

---

**That's it!** You're now ready to use CommandPro. Start analyzing errors and get solutions instantly!

For advanced usage and customization, see the full documentation in `README-CMDPRO.md`.
