# CommandPro Installation & Setup Guide

## Quick Start (Windows PowerShell)

### 1. Install Python (if not already installed)
```powershell
# Download from https://www.python.org/
# Or use Chocolatey:
choco install python
```

### 2. Navigate to CommandPro Directory
```powershell
cd C:\src\cmdpro
```

### 3. Install as Package (Optional)
```powershell
pip install -e .
```

### 4. Test It Works
```powershell
python cli.py "command not found"
```

You should see the error type identified and solutions printed.

## Usage Methods

### Method 1: Direct CLI Usage
```powershell
python C:\src\cmdpro\cli.py "your error message"
```

### Method 2: Interactive Mode
```powershell
python C:\src\cmdpro\cli.py
# Then paste your error message and press Enter twice
```

### Method 3: PowerShell Alias (Recommended)

Add this to your PowerShell profile (`$PROFILE`):

```powershell
# Load CommandPro integration
& "C:\src\cmdpro\cmdpro.ps1"
```

Then use anywhere in PowerShell:
```powershell
err "your error message"
# or
solve "your error message"
```

### Finding Your PowerShell Profile

```powershell
# Check if profile exists
Test-Path $PROFILE

# Create if it doesn't exist
New-Item -Path $PROFILE -Type File -Force

# Edit your profile
notepad $PROFILE
```

## Running Tests

```powershell
cd C:\src\cmdpro
python tests.py
```

Or for verbose output:
```powershell
python tests.py -v
```

## Test the Error Analyzer

Run the test suite to see examples:
```powershell
python test_analyzer.py
```

This will test all 10 supported error types with examples.

## Adding Custom Errors

Edit `knowledge_base.py` and add entries to `ERROR_PATTERNS`:

```python
{
    "name": "Your Error Type",
    "patterns": [
        r"regex_pattern_1",
        r"regex_pattern_2",
    ],
    "solutions": [
        "Solution step 1",
        "Solution step 2",
    ],
    "examples": [
        "Example command 1",
        "Example command 2",
    ]
}
```

## Troubleshooting

### Issue: "ModuleNotFoundError" when running
**Solution**: Make sure you're in the correct directory:
```powershell
cd C:\src\cmdpro
python cli.py "error message"
```

### Issue: Can't load PowerShell profile
**Solution**: Check execution policy:
```powershell
# Allow local scripts to run
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Issue: Python not found
**Solution**: Install Python or add it to PATH:
```powershell
# Check if Python is installed
python --version

# If not found, install via:
# - Direct download: https://www.python.org/
# - Chocolatey: choco install python
```

## Architecture

```
cli.py                  - Entry point, handles input/output
├── analyzer.py         - ErrorAnalyzer class
│   └── knowledge_base.py - Error patterns database
```

## Performance

- Zero dependencies - uses only Python standard library
- Fast pattern matching using regex
- Instant error identification

## Future Enhancements

- [ ] Machine learning for unknown error types
- [ ] Custom knowledge base loading
- [ ] Integration with online resources
- [ ] Database of error solutions
- [ ] GUI interface
- [ ] IDE plugins

## Support

For issues or suggestions:
1. Check `README-CMDPRO.md` for more information
2. Review the knowledge base in `knowledge_base.py`
3. Test with `tests.py`

## License

See LICENSE file in the repository.
