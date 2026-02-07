"""Knowledge base of common errors and solutions"""

ERROR_PATTERNS = [
    {
        "name": "Command Not Found",
        "patterns": [
            r"is not recognized as the name of a cmdlet",
            r"command not found",
            r"'.*?' is not recognized as an internal or external command",
        ],
        "solutions": [
            "The command may not be installed. Check if it's in your PATH.",
            "Try installing the missing tool using package managers (pip, choco, etc.)",
            "Verify the command name is spelled correctly.",
        ],
        "examples": [
            "Check if Python is installed: python --version",
            "Install a missing tool: choco install <package-name>",
        ]
    },
    {
        "name": "File or Directory Not Found",
        "patterns": [
            r"cannot find the path",
            r"No such file or directory",
            r"Path does not exist",
            r"FileNotFoundError",
        ],
        "solutions": [
            "Check if the file/directory path is correct.",
            "Verify the file exists with: ls <path> or dir <path>",
            "Use absolute paths instead of relative paths if possible.",
        ],
        "examples": [
            "List directory contents: dir C:\\path\\to\\folder",
            "Check current directory: pwd",
        ]
    },
    {
        "name": "Permission Denied",
        "patterns": [
            r"Access is denied",
            r"Permission denied",
            r"PermissionError",
            r"You do not have permission",
        ],
        "solutions": [
            "Run the command as Administrator.",
            "Check file permissions with: icacls <file>",
            "Change permissions if needed: icacls <file> /grant Everyone:F",
        ],
        "examples": [
            "Run PowerShell as Admin and retry the command.",
            "Check file permissions: icacls C:\\path\\to\\file",
        ]
    },
    {
        "name": "Port Already in Use",
        "patterns": [
            r"Address already in use",
            r"port .* already in use",
            r"Cannot bind to port",
            r"port is already allocated",
        ],
        "solutions": [
            "Find the process using the port and terminate it.",
            "Use a different port if possible.",
            "Wait a moment and retry (port may be in TIME_WAIT state).",
        ],
        "examples": [
            "Find process on port 8000: netstat -ano | findstr :8000",
            "Kill process: taskkill /PID <pid> /F",
            "Use different port: python app.py --port 8001",
        ]
    },
    {
        "name": "Module or Package Not Found",
        "patterns": [
            r"ModuleNotFoundError",
            r"No module named",
            r"cannot find module",
            r"ImportError",
        ],
        "solutions": [
            "Install the missing package: pip install <package-name>",
            "Check package name spelling.",
            "Ensure you're using the correct Python environment/virtual env.",
        ],
        "examples": [
            "Install a package: pip install requests",
            "Install from requirements file: pip install -r requirements.txt",
        ]
    },
    {
        "name": "Network Connection Error",
        "patterns": [
            r"Connection refused",
            r"Connection timeout",
            r"Unable to connect",
            r"network is unreachable",
        ],
        "solutions": [
            "Check your internet connection.",
            "Verify the server is running and accessible.",
            "Check firewall settings.",
            "Try accessing with a different network (WiFi vs Ethernet).",
        ],
        "examples": [
            "Test connection: ping google.com",
            "Check port connectivity: telnet localhost 8000",
        ]
    },
    {
        "name": "Authentication Failed",
        "patterns": [
            r"authentication failed",
            r"401 Unauthorized",
            r"invalid credentials",
            r"permission denied \(publickey\)",
        ],
        "solutions": [
            "Check your credentials/API keys.",
            "Verify API key or token is valid.",
            "For SSH: ensure correct private key is loaded (ssh-add).",
            "Check username and password.",
        ],
        "examples": [
            "Load SSH key: ssh-add path\\to\\private\\key",
            "Test Git credentials: git ls-remote https://github.com/user/repo",
        ]
    },
    {
        "name": "Syntax Error",
        "patterns": [
            r"SyntaxError",
            r"syntax error",
            r"unexpected token",
            r"missing closing",
        ],
        "solutions": [
            "Check for matching brackets, parentheses, and quotes.",
            "Review the line number indicated in the error.",
            "Check for missing colons after if/for/while statements.",
        ],
        "examples": [
            "Look at the line number: Open file at the error line and check syntax.",
        ]
    },
    {
        "name": "Disk Space Error",
        "patterns": [
            r"no space left on device",
            r"disk full",
            r"out of space",
            r"insufficient space",
        ],
        "solutions": [
            "Check available disk space: disk usage",
            "Delete unnecessary files or move large files.",
            "Clean up temp files: Remove-Item $env:TEMP\\* -Recurse",
        ],
        "examples": [
            "Check disk usage: Get-Volume",
            "Clean temp files: Remove-Item $env:TEMP -Recurse -Force",
        ]
    },
    {
        "name": "Invalid Argument or Option",
        "patterns": [
            r"invalid argument",
            r"unrecognized arguments?",
            r"unknown option",
            r"invalid option",
        ],
        "solutions": [
            "Check command help: <command> --help or <command> -h",
            "Verify argument syntax and order.",
            "Ensure arguments match expected format.",
        ],
        "examples": [
            "Get help: python script.py --help",
            "Check command documentation online.",
        ]
    },
]


def get_all_patterns():
    """Return all error patterns from knowledge base"""
    return ERROR_PATTERNS


def find_error_type(error_message: str) -> dict:
    """Find matching error type for given error message"""
    import re
    
    error_lower = error_message.lower()
    
    for error_type in ERROR_PATTERNS:
        for pattern in error_type.get("patterns", []):
            if re.search(pattern, error_lower, re.IGNORECASE):
                return error_type
    
    return None
