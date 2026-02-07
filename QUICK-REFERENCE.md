# CommandPro Quick Reference

## Installation

```powershell
# No external dependencies needed - uses Python stdlib only!
cd C:\src\cmdpro
pip install -e .  # Optional
```

## Basic Usage

```powershell
# Analyze an error
python cli.py "your error message"

# Interactive mode
python cli.py

# With PowerShell alias (after setup)
err "error message"
solve "error message"
```

## Supported Errors

| Error Type | Common Patterns | Quick Fix |
|---|---|---|
| **Command Not Found** | "not recognized", "command not found" | Install tool, check PATH |
| **File Not Found** | "cannot find", "No such file" | Check path, use absolute path |
| **Permission Denied** | "Access is denied", "Permission denied" | Run as Admin, check perms |
| **Port in Use** | "Address already in use", "port already in use" | Kill process, use diff port |
| **Module Not Found** | "ModuleNotFoundError", "No module named" | `pip install <package>` |
| **Network Error** | "Connection refused", "Connection timeout" | Check internet, restart server |
| **Auth Failed** | "authentication failed", "401 Unauthorized" | Check credentials, validate token |
| **Syntax Error** | "SyntaxError", "unexpected token" | Check brackets, quotes, colons |
| **Disk Full** | "no space left", "disk full" | Clean up, delete files |
| **Invalid Argument** | "invalid argument", "unrecognized arguments" | Check --help, verify syntax |

## Python API

```python
from analyzer import ErrorAnalyzer

# Analyze error
result = ErrorAnalyzer.analyze("error message")

# Check result
if result['success']:
    print(f"Type: {result['error_type']}")
    print(f"Solutions: {result['solutions']}")
    print(f"Examples: {result['examples']}")
```

## PowerShell Setup

Add to `$PROFILE`:
```powershell
& "C:\src\cmdpro\cmdpro.ps1"
# Then use:
err "error message"
```

## Files Reference

| File | Purpose |
|---|---|
| `cli.py` | Main entry point |
| `analyzer.py` | Analysis engine |
| `knowledge_base.py` | Error patterns database |
| `config.py` | Configuration settings |
| `tests.py` | Unit tests |
| `test_analyzer.py` | Integration tests |
| `examples.py` | Usage examples |
| `cmdpro.ps1` | PowerShell integration |

## Running Tests

```powershell
# Unit tests
python tests.py -v

# Integration tests
python test_analyzer.py

# Examples
python examples.py
```

## Common Tasks

### Add Custom Error
Edit `knowledge_base.py`:
```python
{
    "name": "Your Error",
    "patterns": [r"error pattern"],
    "solutions": ["Step 1", "Step 2"],
    "examples": ["Example command"],
}
```

### Run Programmatically
```python
from analyzer import ErrorAnalyzer

errors = [
    "command not found",
    "access denied",
    "ModuleNotFoundError"
]

for error in errors:
    result = ErrorAnalyzer.analyze(error)
    print(f"{result['error_type']}: {result['solutions'][0]}")
```

### Check Supported Types
```python
from knowledge_base import get_all_patterns

for pattern in get_all_patterns():
    print(pattern['name'])
```

## Troubleshooting

| Problem | Solution |
|---|---|
| Module not found | `cd C:\src\cmdpro` before running |
| Python not found | Install Python, add to PATH |
| PowerShell profile error | Run: `Set-ExecutionPolicy RemoteSigned -Scope CurrentUser` |
| Tests fail | Check Python version >= 3.7 |

## Output Example

```
============================================================
CommandPro - Error Helper
============================================================

✓ Error Type: Module or Package Not Found

Suggested Solutions:
  1. Install the missing package: pip install <package-name>
  2. Check package name spelling.
  3. Ensure you're using the correct Python environment/virtual env.

Try These Examples:
  1. Install a package: pip install requests
  2. Install from requirements file: pip install -r requirements.txt
```

## Performance

- ⚡ Instant error identification (regex matching)
- 📦 Zero external dependencies
- 🔄 Pattern-based matching
- 💾 < 1MB total size

## Advanced Usage

See `examples.py` for:
- Batch processing
- Custom wrappers
- Error confidence scoring
- Integration patterns
- Programmatic usage

---

For more details: See README-CMDPRO.md, INSTALL.md, and examples.py
