# CommandPro - Command Line Error Helper

A Python-based command line helper that analyzes error messages and provides helpful solutions for common command errors, especially in Windows PowerShell.

## Features

- **Error Recognition**: Identifies common error types from error messages
- **Solution Suggestions**: Provides practical solutions for each error type
- **Examples**: Shows real-world examples of how to fix errors
- **Interactive & CLI Modes**: Use interactively or pass error as argument
- **No Dependencies**: Uses only Python standard library

## Installation

### Option 1: Install as Package

```bash
cd C:\src\cmdpro
pip install -e .
```

Then use globally:
```powershell
cmdpro "your error message"
```

### Option 2: Run Directly

```powershell
cd C:\src\cmdpro
python cli.py "your error message"
```

## Usage

### Interactive Mode
Simply run without arguments and paste your error message:

```powershell
python cli.py
```

Then paste your error message and press Enter twice to submit.

### Command Line Mode
Pass the error message as an argument:

```powershell
python cli.py "command not found: python3"
```

## Supported Error Types

1. **Command Not Found** - When a command/tool is not recognized
2. **File or Directory Not Found** - Path issues
3. **Permission Denied** - Access control issues
4. **Port Already in Use** - Network binding conflicts
5. **Module or Package Not Found** - Missing Python packages/modules
6. **Network Connection Error** - Connectivity issues
7. **Authentication Failed** - Credential/token issues
8. **Syntax Error** - Code syntax problems
9. **Disk Space Error** - Storage issues
10. **Invalid Argument or Option** - Command argument problems

## Example Output

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

## Adding New Error Types

Edit `knowledge_base.py` and add entries to the `ERROR_PATTERNS` list:

```python
{
    "name": "Your Error Type",
    "patterns": [
        r"regex pattern 1",
        r"regex pattern 2",
    ],
    "solutions": [
        "Solution 1",
        "Solution 2",
    ],
    "examples": [
        "Example 1: command",
        "Example 2: command",
    ]
}
```

## PowerShell Integration

Create a PowerShell function for easy access. Add to your PowerShell profile:

```powershell
function Solve-Error {
    param(
        [Parameter(ValueFromRemainingArguments=$true)]
        [string]$ErrorMessage
    )
    
    if ($ErrorMessage) {
        python "C:\src\cmdpro\cli.py" $ErrorMessage
    }
    else {
        python "C:\src\cmdpro\cli.py"
    }
}

Set-Alias -Name err -Value Solve-Error
```

Then use in PowerShell:
```powershell
err "command not found: xyz"
# or alias
err command not found xyz
```

## Project Structure

```
cmdpro/
├── __init__.py           # Package initialization
├── cli.py                # Command line interface
├── analyzer.py           # Error analysis logic
├── knowledge_base.py     # Error patterns and solutions
├── setup.py              # Package setup configuration
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## Development

To test the error analyzer:

```powershell
python -c "from analyzer import ErrorAnalyzer; print(ErrorAnalyzer.analyze('command not found'))"
```

## License

MIT License - See LICENSE file for details

## Contributing

1. Test new error patterns thoroughly
2. Keep solutions practical and actionable
3. Add relevant examples for each error type
4. Test with real-world error messages
