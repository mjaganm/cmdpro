"""
Enhanced CLI with ML-powered error analysis

Combines rule-based (CommandPro) and ML-based (Ollama) error fixing.
"""

import sys
from typing import Optional, Dict, Any
from analyzer import ErrorAnalyzer
from stream_processor import CommandWrapper, RealTimeDisplay
from ollama_client import OllamaClient, OllamaManager
from ml_config import FEATURES, FALLBACK_CONFIG, DISPLAY_CONFIG


class MLErrorProcessor:
    """Process errors using ML with fallback to rule-based system"""
    
    def __init__(self):
        self.ollama_client = OllamaClient() if FEATURES.get("use_ml") else None
        self.use_fallback = FEATURES.get("use_fallback", True)
        self.display = RealTimeDisplay()
    
    def process_error(self, error_message: str, command_context: str = "") -> Dict[str, Any]:
        """
        Process an error using ML and/or rule-based analysis
        
        Args:
            error_message: The error output
            command_context: The command that was run
            
        Returns:
            Analysis result with suggestions
        """
        result = {
            "success": False,
            "method": None,
            "error_type": None,
            "suggestions": [],
            "ml_confidence": 0.0
        }
        
        # Try ML first if enabled and available
        if FEATURES.get("use_ml") and self.ollama_client and self.ollama_client.is_available():
            ml_suggestion = self._get_ml_suggestion(error_message, command_context)
            if ml_suggestion:
                result["success"] = True
                result["method"] = "ML"
                result["suggestions"] = [ml_suggestion]
                result["ml_confidence"] = 0.85
                return result
        
        # Fallback to rule-based if enabled
        if self.use_fallback:
            rule_result = ErrorAnalyzer.analyze(error_message)
            if rule_result["success"]:
                result["success"] = True
                result["method"] = "Rule-Based"
                result["error_type"] = rule_result.get("error_type")
                result["suggestions"] = rule_result.get("solutions", [])
                if "examples" in rule_result:
                    result["examples"] = rule_result["examples"]
                return result
        
        # No suggestions available
        result["suggestions"] = [
            "Try searching online for this error message",
            "Check the official documentation",
            "Verify your inputs are correct"
        ]
        return result
    
    def _get_ml_suggestion(self, error_message: str, context: str = "") -> Optional[str]:
        """Get suggestion from ML model"""
        try:
            if FEATURES.get("stream_responses"):
                # Stream the response in real-time
                suggestion_parts = []
                for chunk in self.ollama_client.analyze_error_stream(error_message, context):
                    suggestion_parts.append(chunk)
                    # Print chunks as they arrive for real-time feedback
                    if DISPLAY_CONFIG.get("verbose"):
                        print(chunk, end='', flush=True)
                return "".join(suggestion_parts).strip()
            else:
                # Get complete response at once
                return self.ollama_client.analyze_error(error_message, context)
        except Exception as e:
            if FEATURES.get("use_fallback"):
                print(f"ML analysis failed, falling back to rule-based")
            return None


class EnhancedCLI:
    """Enhanced CLI with command wrapping and ML analysis"""
    
    def __init__(self):
        self.processor = MLErrorProcessor()
        self.display = RealTimeDisplay()
        self.wrapper = CommandWrapper()
    
    def run_command_with_analysis(self, command: str) -> int:
        """
        Run a command and analyze any errors with ML
        
        Args:
            command: Command to execute
            
        Returns:
            Command return code
        """
        print(f"🔧 Running: {command}\n")
        
        # Track stderr chunks for analysis
        stderr_chunks = []
        
        def on_stderr_chunk(chunk):
            """Callback for stderr chunks"""
            stderr_chunks.append(chunk)
            # Could process in real-time here
            print(chunk, end='', flush=True)
        
        # Run the command
        result = self.wrapper.run_with_capture(
            command,
            on_stderr_chunk=on_stderr_chunk,
            shell=True
        )
        
        # Analyze if there was an error
        if not result["success"] and result["stderr"]:
            print("\n" + "=" * 70)
            print("Analyzing error with CommandPro ML...")
            print("=" * 70 + "\n")
            
            analysis = self.processor.process_error(
                result["stderr"],
                command_context=command
            )
            
            self._display_analysis(analysis)
        
        return result["returncode"]
    
    def _display_analysis(self, analysis: Dict[str, Any]):
        """Display analysis results"""
        if not analysis["success"]:
            print("Could not identify error type.")
            return
        
        print(f"\n✓ Method: {analysis['method']}")
        if analysis.get("error_type"):
            print(f"✓ Error Type: {analysis['error_type']}")
        if analysis.get("ml_confidence"):
            print(f"✓ Confidence: {analysis['ml_confidence']*100:.0f}%")
        
        print("\n💡 Suggested Fixes:")
        for i, suggestion in enumerate(analysis["suggestions"], 1):
            print(f"  {i}. {suggestion}")
        
        if "examples" in analysis:
            print("\n📝 Examples:")
            for i, example in enumerate(analysis["examples"], 1):
                print(f"  {i}. {example}")
        
        print()


def main():
    """Main entry point for enhanced CLI"""
    
    # Check if Ollama is available
    if FEATURES.get("use_ml"):
        if not OllamaManager.is_running():
            print("⚠️  Ollama is not running. Using rule-based analysis only.")
            print("   Tip: Start Ollama with: ollama serve")
            print("   Or pull a model with: ollama pull mistral\n")
    
    # Get command from arguments
    if len(sys.argv) < 2:
        print("Usage: python ml_cli.py <command>")
        print("Example: python ml_cli.py 'npm install missing-package'")
        return 1
    
    command = " ".join(sys.argv[1:])
    
    # Run with analysis
    cli = EnhancedCLI()
    return_code = cli.run_command_with_analysis(command)
    
    return return_code


if __name__ == "__main__":
    sys.exit(main())
