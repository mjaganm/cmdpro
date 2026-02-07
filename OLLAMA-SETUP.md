╔════════════════════════════════════════════════════════════════════════════╗
║                                                                            ║
║                 OLLAMA SETUP - IMPORTANT INFORMATION                       ║
║                                                                            ║
╚════════════════════════════════════════════════════════════════════════════╝

📌 ENVIRONMENT LIMITATION DETECTED
═══════════════════════════════════════════════════════════════════════════════

The current environment does not have PowerShell 6+ available for running
background servers. However, you can still use CommandPro ML easily!

🔧 HOW TO SET UP OLLAMA ON YOUR LOCAL MACHINE
═══════════════════════════════════════════════════════════════════════════════

Since you're using this on a Windows system, follow these steps:

STEP 1: Download Ollama
────────────────────────
1. Visit https://ollama.ai
2. Download the Windows installer
3. Run the installer and follow prompts
4. This installs Ollama locally

STEP 2: Start Ollama Server (on your computer)
───────────────────────────────────────────────
Option A - Using Command Prompt/PowerShell on your PC:
  1. Open Command Prompt or PowerShell on your Windows machine
  2. Run: ollama serve
  3. Keep this window open (it's your AI server)

Option B - Let Ollama start automatically:
  1. Ollama may auto-start as a service after installation
  2. Check by visiting: http://localhost:11434/api/tags in browser
  3. If you get a response, it's running!

STEP 3: Download a Model (in another terminal)
────────────────────────────────────────────────
1. Open another Command Prompt/PowerShell
2. Run: ollama pull mistral
   (This downloads ~5GB, takes 2-3 minutes)
3. When done, you're ready!

STEP 4: Test the Setup
──────────────────────
cd C:\src\cmdpro
python ml_cli.py "python --invalid-option"

You should see AI-powered error analysis!


✅ WHAT YOU'LL HAVE AFTER SETUP
═══════════════════════════════════════════════════════════════════════════════

Terminal 1:
  ollama serve → Running Ollama server (keep open)

Terminal 2:
  Ready to run commands with AI analysis

Terminal 3:
  Ready to use CommandPro ML


🎯 QUICK COMMANDS TO RUN ON YOUR MACHINE
═══════════════════════════════════════════════════════════════════════════════

# Check if Ollama is running:
curl http://localhost:11434/api/tags

# Download a model:
ollama pull mistral

# See available models:
ollama list

# Test analysis:
cd C:\src\cmdpro
python ml_cli.py "npm install missing-package"


📋 MANUAL TESTING WITHOUT OLLAMA
═══════════════════════════════════════════════════════════════════════════════

You can still test CommandPro (rule-based) right now:

# Test rule-based analysis:
cd C:\src\cmdpro
python cli.py "ModuleNotFoundError"

# Or run examples:
python ml_examples.py

These work without Ollama!


🔄 HYBRID FALLBACK SYSTEM
═══════════════════════════════════════════════════════════════════════════════

CommandPro ML is smart - it works BOTH ways:

WITH Ollama running:
  python ml_cli.py "error" → AI analysis + streaming suggestions

WITHOUT Ollama running:
  python ml_cli.py "error" → Automatic fallback to rule-based (CommandPro)

You get AI when available, reliability when not!


📊 WHAT WILL HAPPEN WHEN OLLAMA IS RUNNING
═══════════════════════════════════════════════════════════════════════════════

When you run on your machine with Ollama:

$ python ml_cli.py "python --invalid-option"

1. CommandPro captures the error from stderr
2. Sends to Ollama at http://localhost:11434
3. Ollama analyzes with Mistral model
4. Streams intelligent suggestion back
5. Displays fix in real-time

All on your machine. No external APIs.


🚀 READY TO GO
═══════════════════════════════════════════════════════════════════════════════

1. Install Ollama: https://ollama.ai
2. Run: ollama serve
3. Run: ollama pull mistral
4. Test: python ml_cli.py "error"

Or just use rule-based:
  python cli.py "error"

Everything is ready in C:\src\cmdpro!


❓ QUESTIONS?
═══════════════════════════════════════════════════════════════════════════════

Q: Can I test without installing Ollama?
A: Yes! Use: python cli.py "error" (rule-based, works instantly)

Q: When should I use ML vs rule-based?
A: ML (Ollama) for complex errors, rule-based for instant analysis

Q: Is Ollama hard to install?
A: No, just download and run the installer from ollama.ai

Q: Do I need all 5GB for the model?
A: Yes, Mistral is ~5GB. Smaller models available (3.5GB - 13GB+)

Q: What if I don't have Ollama running?
A: Falls back to rule-based automatically - no issues!


═══════════════════════════════════════════════════════════════════════════════

Next step: Install Ollama and run these commands on your Windows machine:

1. ollama serve
2. ollama pull mistral
3. python ml_cli.py "your error"

Everything is ready in C:\src\cmdpro! 🚀
