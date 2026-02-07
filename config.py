"""
Configuration file for CommandPro

Customize behavior by editing settings here.
"""

# Display settings
SHOW_EXAMPLES = True
SHOW_ORIGINAL_ERROR = False
MAX_SOLUTIONS_SHOWN = 5

# Pattern matching settings
CASE_INSENSITIVE_MATCHING = True
USE_REGEX = True

# Color output (for terminal)
USE_COLORS = True

# Logging
VERBOSE_MODE = False
LOG_FILE = None  # Set to file path to enable logging

# Advanced settings
CONFIDENCE_THRESHOLD = 0.5  # Minimum confidence to display a match
CACHE_RESULTS = False  # Cache analysis results

# Custom error patterns file (optional)
CUSTOM_PATTERNS_FILE = None  # Path to JSON file with custom patterns

# PowerShell specific settings
POWERSHELL_INTEGRATION = True
SHOW_POWERSHELL_EXAMPLES = True
