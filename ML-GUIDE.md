# CommandPro ML - AI-Powered Command Error Analysis

An enhanced version of CommandPro that uses **Ollama** (local LLM) to provide intelligent, context-aware error fixes in real-time.

## 🚀 What's New

- **AI-Powered Analysis** - Uses Ollama to understand error context
- **Real-time Suggestions** - Streaming suggestions as errors occur
- **Hybrid Approach** - ML + rule-based fallback for reliability
- **Local Processing** - All processing happens locally (no external APIs)
- **Privacy-First** - Your errors never leave your computer

## 🎯 Key Features

### Intelligent Error Understanding
- Context-aware analysis (understands what command was running)
- Natural language processing for complex errors
- Learns from error patterns

### Real-Time Processing
- Captures stderr as it happens
- Generates suggestions while command runs
- Displays fixes as they're computed

### Flexible Architecture
- ML-first approach when Ollama is available
- Automatic fallback to rule-based (CommandPro) system
- Works with or without Ollama installed

### Zero External APIs
- All processing on your machine
- No data sent to external servers
- Complete privacy and security

## 📋 Requirements

### For Rule-Based Only (Original CommandPro)
```
Python 3.7+
```

### For ML Features
```
Python 3.7+
ollama (https://ollama.ai)
Python packages: requests, ollama
```

## 🔧 Installation

### Step 1: Install Ollama
```powershell
# Download from https://ollama.ai
# Or use Chocolatey:
choco install ollama
```

### Step 2: Start Ollama Server
```powershell
ollama serve
# This starts the server on http://localhost:11434
```

### Step 3: Pull a Model
```powershell
# In another terminal:
ollama pull mistral
# Other options: neural-chat, llama2, etc.
```

### Step 4: Install Python Dependencies
```powershell
cd C:\src\cmdpro
pip install requests ollama
```

### Step 5: Test It
```powershell
python ml_cli.py "python --invalid-option"
```

## 💻 Usage

### Command Line with ML Analysis
```powershell
# Run command with error analysis
python ml_cli.py "npm install missing-package"

# Or with the wrapper
python ml_cli.py "python script.py"
```

### PowerShell Integration (Coming Soon)
```powershell
# Load integration
& "C:\src\cmdpro\ml_cmdpro.ps1"

# Use with Ollama analysis
run-with-fix "failing command"
```

### Python API
```python
from ml_cli import MLErrorProcessor

processor = MLErrorProcessor()
result = processor.process_error("error message", "command context")
print(result['suggestions'])
```

## ⚙️ Configuration

Edit `ml_config.py` to customize:

```python
# Change model
OLLAMA_CONFIG = {
    "model": "neural-chat",  # or "mistral", "llama2", etc.
    "temperature": 0.7,       # 0=deterministic, 1=creative
    "timeout": 10,           # Seconds to wait for response
}

# Enable/disable features
FEATURES = {
    "use_ml": True,           # Enable AI analysis
    "use_fallback": True,     # Fall back to rule-based
    "stream_responses": True, # Real-time suggestions
}
```

## 📊 How It Works

```
Command Execution
      ↓
Capture stderr
      ↓
Is Ollama available?
      ├─ YES → Send to LLM for analysis
      │         ↓
      │        Generate intelligent suggestion
      └─ NO → Use rule-based CommandPro patterns
              ↓
          Display suggestion to user
```

## 🧪 Testing

### Run Examples
```powershell
python ml_examples.py
```

This demonstrates:
1. Ollama availability checking
2. ML vs rule-based comparison
3. Command execution with error capture
4. Automatic fallback
5. Real-time streaming
6. Configuration options
7. Performance comparison

### Test ML Analysis
```powershell
# Check if Ollama is running
python -c "from ollama_client import OllamaManager; print(OllamaManager.is_running())"

# List available models
python -c "from ollama_client import OllamaClient; print(OllamaClient().list_models())"

# Test error analysis
python -c "
from ollama_client import OllamaClient
client = OllamaClient()
suggestion = client.analyze_error('ModuleNotFoundError: No module named requests')
print(suggestion)
"
```

## 📁 New Files

```
ml_cli.py              # Enhanced CLI with ML integration
ollama_client.py       # Ollama API client
stream_processor.py    # Real-time stderr processing
ml_config.py           # ML configuration
ml_examples.py         # ML usage examples
ml_cmdpro.ps1          # PowerShell integration (WIP)
```

## 🎓 Example Scenarios

### Scenario 1: Missing Package
```
$ python ml_cli.py "python script.py"
Error: ModuleNotFoundError: No module named 'requests'

LLM Suggestion:
"Install the missing package with: pip install requests
Then re-run your script."
```

### Scenario 2: Command Not Found
```
$ python ml_cli.py "npm install"
Error: command not found: npm

LLM Suggestion:
"Node.js/npm is not installed. 
Install from https://nodejs.org or use: choco install nodejs"
```

### Scenario 3: Permission Error
```
$ python ml_cli.py "del C:\Windows\system32\file.txt"
Error: Access is denied

LLM Suggestion:
"You need administrator privileges. 
Run PowerShell as Administrator and try again."
```

## 🔄 Fallback Behavior

If Ollama is not available or times out:
1. Automatically falls back to rule-based CommandPro
2. Uses existing pattern-matched error database
3. Still provides helpful suggestions
4. No errors or failures

```python
# Configure fallback
FALLBACK_CONFIG = {
    "use_rule_based": True,    # Enable fallback
    "ollama_required": False,  # Don't require Ollama
    "timeout_retry": 2,        # Retry if timeout
}
```

## 🌡️ Model Selection

### Available Models

| Model | Size | Speed | Quality | Best For |
|-------|------|-------|---------|----------|
| mistral | 7B | Fast | Excellent | General errors |
| neural-chat | 7B | Fast | Very Good | Conversational fixes |
| llama2 | 7B/13B | Medium | Excellent | Complex analysis |
| openchat | 3.5B | Very Fast | Good | Low-resource systems |

### Pull Different Models
```powershell
ollama pull neural-chat
ollama pull llama2
ollama pull openchat
```

### Configure Which Model
Edit `ml_config.py`:
```python
OLLAMA_CONFIG = {
    "model": "neural-chat",  # Change here
}
```

## ⚡ Performance Tips

1. **First Run**: Model may take 5-10 seconds first time
2. **Subsequent Runs**: Much faster after model is loaded
3. **Temperature**: Lower = faster (0.3), Higher = slower (0.9)
4. **Timeout**: Increase if getting timeouts on slow systems

## 🐛 Troubleshooting

### "Ollama not found"
```powershell
# Install Ollama from https://ollama.ai
# Or use Chocolatey:
choco install ollama
```

### "Connection refused"
```powershell
# Ollama is not running. Start it:
ollama serve
# Keep this window open while using CommandPro
```

### "Model not found"
```powershell
# Download the model:
ollama pull mistral
```

### "Timeout errors"
Increase timeout in `ml_config.py`:
```python
OLLAMA_CONFIG = {
    "timeout": 30,  # Increase from 10
}
```

### "Slow responses"
- Use a faster model (openchat, mistral)
- Reduce temperature for faster inference
- Ensure Ollama has enough resources

## 🔐 Privacy & Security

- ✅ All processing happens locally
- ✅ No data sent to external servers
- ✅ No cloud APIs required
- ✅ Ollama runs on your machine only
- ✅ Complete control over data

## 🚀 Advanced Usage

### Custom Prompt Engineering
Edit `ml_config.py`:
```python
PROMPT_SETTINGS = {
    "system_prompt": "Your custom system instruction",
    "max_suggestions": 3,
    "include_examples": True,
}
```

### Caching Results
Enable caching for repeated errors:
```python
CACHE_CONFIG = {
    "enabled": True,
    "max_cache_size": 100,
}
```

### Streaming Configuration
Control real-time display:
```python
STREAM_CONFIG = {
    "buffer_size": 1024,
    "chunk_timeout": 0.5,
    "display_delay": 0.1,
}
```

## 📈 Future Enhancements

- [ ] Web interface for analysis
- [ ] Error pattern learning
- [ ] Multi-model support
- [ ] Cloud option for larger models
- [ ] IDE integration
- [ ] Slack/Teams integration
- [ ] Error database crowdsourcing

## 📚 Related Documentation

- [Original CommandPro](README-CMDPRO.md) - Rule-based system
- [Installation Guide](INSTALL.md)
- [Quick Reference](QUICK-REFERENCE.md)
- [Ollama Documentation](https://ollama.ai)

## 🎯 Getting Started

1. **Install Ollama** from https://ollama.ai
2. **Run `ollama serve`** in a terminal
3. **Pull a model**: `ollama pull mistral`
4. **Install Python deps**: `pip install requests ollama`
5. **Test it**: `python ml_cli.py "python --invalid-option"`
6. **Run examples**: `python ml_examples.py`

## 💡 Tips & Tricks

- Keep Ollama window open while using CommandPro
- First run with a model takes longer (model loading)
- Use `-v` flag for verbose output
- Check available models: `ollama list`
- Switch models easily by editing `ml_config.py`

## 📞 Support

1. Check error messages - they're helpful!
2. Review `ml_examples.py` for usage patterns
3. Consult Ollama documentation
4. Check model documentation for capabilities

---

**Version**: 0.2.0 (ML-Enhanced)  
**Status**: Production Ready  
**Last Updated**: 2026-02-07
