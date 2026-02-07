# CommandPro ML - Quick Start Guide

Get AI-powered error fixing running in 10 minutes!

## 🎯 What You Need

1. **Ollama** - Local AI model server (free, open-source)
2. **Python 3.7+** - Already installed
3. **2 Python packages** - requests, ollama

## ⚡ 10-Minute Setup

### Step 1: Download & Install Ollama (2 minutes)

```powershell
# Option A: Direct download
# Visit https://ollama.ai and download installer

# Option B: Using Chocolatey
choco install ollama
```

### Step 2: Start Ollama Server (1 minute)

```powershell
ollama serve
# Keep this window open - it's your AI server!
```

### Step 3: Download a Model (3 minutes)

Open **another PowerShell window**:

```powershell
ollama pull mistral
# This downloads the AI model (~5GB, takes 2-3 minutes)
```

### Step 4: Install Python Packages (1 minute)

```powershell
cd C:\src\cmdpro
pip install requests ollama
```

### Step 5: Test It Works (1 minute)

```powershell
# Try a command that will fail
python ml_cli.py "python --invalid-option"
```

You should see:
1. The command running
2. The error captured
3. AI analysis and suggested fix

**Done! You now have CommandPro ML working!** 🎉

## 💻 How to Use

### Method 1: Command Line (Direct)

```powershell
python ml_cli.py "your command here"
python ml_cli.py "npm install missing-package"
```

### Method 2: PowerShell Integration (Recommended)

```powershell
# Load CommandPro ML
& "C:\src\cmdpro\ml_cmdpro.ps1"

# Now use anywhere in PowerShell:
fix "failing command"
fix npm install nonexistent
```

### Method 3: In Your Python Code

```python
from ml_cli import MLErrorProcessor

processor = MLErrorProcessor()
result = processor.process_error("error message", "context")
print(result['suggestions'])
```

## 🧪 Test Examples

### Try These Commands (They Will Fail, That's Okay!)

```powershell
# Test 1: Module not found
python ml_cli.py "python -c \"import nonexistent\""

# Test 2: Command not found
python ml_cli.py "nonexistent-command --help"

# Test 3: Permission error (Windows)
python ml_cli.py "del C:\Windows\system32\important.txt"

# Test 4: Using with real workflow
python ml_cli.py "pip install package-that-does-not-exist"
```

Each will:
1. Run and fail
2. Capture the error
3. Send to Ollama AI
4. Display intelligent suggestion

## ⚙️ What Happens Under the Hood

```
Your Command
    ↓
CommandPro captures stderr
    ↓
Is Ollama available? (YES if step 2 still running)
    ↓
Send error to local AI model
    ↓
AI analyzes and suggests fix
    ↓
Display suggestion to you
```

## 🎓 First Time Troubleshooting

### "Connection refused"
```
❌ Ollama server isn't running

✅ Solution: Keep the "ollama serve" window open
   Or restart it: ollama serve
```

### "Model not found"
```
❌ You didn't download a model

✅ Solution: In another PowerShell:
   ollama pull mistral
```

### "ModuleNotFoundError: No module named 'requests'"
```
❌ Python package not installed

✅ Solution:
   pip install requests ollama
```

### Slow Responses
```
❌ First run takes longer (model loading)
❌ Your system might be slow

✅ Solutions:
   • Wait 5-10 seconds first time
   • Try smaller model: ollama pull openchat
   • Close other apps
```

## 📊 What Models Are Available?

| Model | Size | Speed | Best For |
|-------|------|-------|----------|
| **mistral** | 7B | ⚡⚡⚡ Fast | General use (recommended) |
| neural-chat | 7B | ⚡⚡⚡ Fast | Conversational |
| openchat | 3.5B | ⚡⚡⚡⚡ Very fast | Low-resource systems |
| llama2 | 7B/13B | ⚡⚡ Medium | Very smart |

### Try Different Models

```powershell
# Switch model by editing ml_config.py:

# Find this section:
OLLAMA_CONFIG = {
    "model": "mistral",  # Change here
}

# Change to:
OLLAMA_CONFIG = {
    "model": "neural-chat",  # or "openchat", "llama2"
}
```

## 🔄 Hybrid Mode (Smart Fallback)

CommandPro ML is smart:
- **If Ollama is running** → Uses AI analysis (smarter, more context-aware)
- **If Ollama is not running** → Falls back to rule-based system (fast, always works)

This means you don't need Ollama to run - CommandPro still works!

```powershell
# Without Ollama (just rule-based):
python ml_cli.py "error message"

# With Ollama (AI-powered):
ollama serve  # In separate window
python ml_cli.py "error message"  # Much smarter analysis!
```

## 🚀 PowerShell Integration Setup (5 minutes)

Make `fix` command work anywhere in PowerShell:

### Option A: Temporary (this session only)
```powershell
& "C:\src\cmdpro\ml_cmdpro.ps1"
fix "your command"  # Now works!
```

### Option B: Permanent (all future sessions)

1. Find your PowerShell profile:
   ```powershell
   $PROFILE
   # Example: C:\Users\YourName\Documents\PowerShell\profile.ps1
   ```

2. Open it in Notepad:
   ```powershell
   notepad $PROFILE
   ```

3. Add this line:
   ```powershell
   & "C:\src\cmdpro\ml_cmdpro.ps1"
   ```

4. Save and restart PowerShell

Now you can use `fix` anywhere! 🎉

## 📚 Learn More

- **Full ML Guide**: Read `ML-GUIDE.md` in cmdpro folder
- **Original CommandPro**: See `README-CMDPRO.md`
- **All Options**: See `QUICK-REFERENCE.md`
- **Examples**: Run `python ml_examples.py`

## 💡 Pro Tips

1. **Keep Ollama window open** - It's your AI server
2. **First run is slow** - Model takes 5-10 seconds to load
3. **Subsequent runs are fast** - Usually <2 seconds
4. **Custom models** - Try `ollama pull neural-chat`
5. **No data sharing** - Everything stays on your computer

## 🎯 Next Steps

1. ✅ Install Ollama
2. ✅ Start `ollama serve`
3. ✅ Download model: `ollama pull mistral`
4. ✅ Install packages: `pip install requests ollama`
5. ✅ Try it: `python ml_cli.py "error"`
6. ✅ Set up PowerShell (optional but nice)
7. ✅ Start using! `fix "command"`

## ❓ Common Questions

**Q: Do I need an API key?**
A: No! Everything runs locally on your computer.

**Q: Is it private?**
A: Completely! No data leaves your machine.

**Q: What if Ollama stops?**
A: Falls back to rule-based CommandPro automatically.

**Q: Can I use different models?**
A: Yes! Download any Ollama model and configure it.

**Q: How much disk space?**
A: Models are 3-7GB. Check your space before downloading.

**Q: Will it slow down my system?**
A: Ollama uses spare CPU/RAM. Minimal impact.

**Q: Can I run multiple models?**
A: Yes, configure in `ml_config.py`.

## 🆘 Still Having Issues?

1. **Check Ollama is running**: Look for `ollama serve` window
2. **Verify model is downloaded**: `ollama list`
3. **Test direct analysis**: `python ml_examples.py`
4. **Check your firewall**: Ensure `localhost:11434` works
5. **Read ML-GUIDE.md**: Full documentation and troubleshooting

## 🎉 You're Ready!

You now have CommandPro ML running with local AI! Start using it:

```powershell
# Quick test
python ml_cli.py "python --invalid-flag"

# Or with PowerShell integration
& "C:\src\cmdpro\ml_cmdpro.ps1"
fix "npm install"
```

Enjoy intelligent error analysis! 🚀

---

**Version**: 0.2.0 (ML)  
**Setup Time**: ~10 minutes  
**Ongoing Time**: Instant when running
