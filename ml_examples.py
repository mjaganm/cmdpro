#!/usr/bin/env python3
"""
ML-powered CommandPro Examples

Demonstrates the new ML capabilities using Ollama.
"""

from ollama_client import OllamaClient, OllamaManager
from stream_processor import CommandWrapper
from ml_config import FEATURES, OLLAMA_CONFIG
from analyzer import ErrorAnalyzer
from ml_cli import MLErrorProcessor


def example_1_ollama_check():
    """Example 1: Check Ollama availability"""
    print("=" * 70)
    print("Example 1: Checking Ollama Availability")
    print("=" * 70)
    
    if OllamaManager.is_running():
        print("✓ Ollama is running")
        client = OllamaClient()
        models = client.list_models()
        print(f"✓ Available models: {models}")
    else:
        print("✗ Ollama is not running")
        print("  To use ML features, install and start Ollama:")
        print("  1. Download from: https://ollama.ai")
        print("  2. Run: ollama serve")
        print("  3. Pull a model: ollama pull mistral")


def example_2_ml_vs_rule_based():
    """Example 2: Compare ML and rule-based analysis"""
    print("\n" + "=" * 70)
    print("Example 2: ML vs Rule-Based Analysis")
    print("=" * 70)
    
    test_errors = [
        "ModuleNotFoundError: No module named 'requests'",
        "command not found: python3",
        "Access is denied",
    ]
    
    processor = MLErrorProcessor()
    
    for error in test_errors:
        print(f"\n📌 Error: {error}")
        print("-" * 70)
        
        analysis = processor.process_error(error)
        print(f"Method: {analysis['method']}")
        print(f"Suggestions: {analysis['suggestions']}")


def example_3_command_execution():
    """Example 3: Run command and capture errors"""
    print("\n" + "=" * 70)
    print("Example 3: Command Execution with Error Capture")
    print("=" * 70)
    
    # This will try to run a command that fails
    # Using a safe, cross-platform command
    test_commands = [
        "python --invalid-option",  # This will produce an error
        "ping invalid_hostname_12345",  # This will fail
    ]
    
    wrapper = CommandWrapper()
    
    for cmd in test_commands[:1]:  # Just run first one for safety
        print(f"\n🔧 Running: {cmd}")
        result = wrapper.run_with_capture(cmd)
        
        print(f"Return code: {result['returncode']}")
        if result['stderr']:
            print(f"Error captured: {result['stderr'][:100]}...")


def example_4_ml_analysis_with_fallback():
    """Example 4: ML analysis with automatic fallback"""
    print("\n" + "=" * 70)
    print("Example 4: ML Analysis with Fallback")
    print("=" * 70)
    
    processor = MLErrorProcessor()
    
    error = "command not found: nonexistent_tool"
    print(f"\nAnalyzing: {error}")
    
    result = processor.process_error(error)
    
    print(f"\n✓ Success: {result['success']}")
    print(f"✓ Method: {result['method']}")
    print(f"✓ Suggestions:")
    for i, suggestion in enumerate(result['suggestions'], 1):
        print(f"  {i}. {suggestion}")


def example_5_streaming():
    """Example 5: Real-time streaming suggestions"""
    print("\n" + "=" * 70)
    print("Example 5: Real-time Streaming (if Ollama available)")
    print("=" * 70)
    
    client = OllamaClient()
    
    if not client.is_available():
        print("Ollama not available - skipping streaming example")
        return
    
    error_msg = "ModuleNotFoundError: No module named numpy"
    print(f"\nAnalyzing: {error_msg}")
    print("Streaming response from LLM...")
    print("-" * 70)
    
    chunks = list(client.analyze_error_stream(error_msg))
    if chunks:
        print("".join(chunks))
    else:
        print("(No response from LLM)")


def example_6_configuration():
    """Example 6: Configuration options"""
    print("\n" + "=" * 70)
    print("Example 6: Configuration Options")
    print("=" * 70)
    
    print("\nCurrent ML Configuration:")
    print(f"  Model: {OLLAMA_CONFIG['model']}")
    print(f"  Base URL: {OLLAMA_CONFIG['base_url']}")
    print(f"  Timeout: {OLLAMA_CONFIG['timeout']}s")
    print(f"  Temperature: {OLLAMA_CONFIG['temperature']}")
    
    print("\nFeature Flags:")
    for feature, enabled in FEATURES.items():
        status = "✓" if enabled else "✗"
        print(f"  {status} {feature}: {enabled}")
    
    print("\nTo customize:")
    print("  Edit ml_config.py and modify settings as needed")


def example_7_performance():
    """Example 7: Performance comparison"""
    print("\n" + "=" * 70)
    print("Example 7: Performance Comparison")
    print("=" * 70)
    
    import time
    
    error = "ModuleNotFoundError: No module named requests"
    
    # Test rule-based speed
    print("\n🚀 Rule-based analysis speed:")
    start = time.time()
    result = ErrorAnalyzer.analyze(error)
    elapsed = time.time() - start
    print(f"  Time: {elapsed*1000:.2f}ms")
    print(f"  Type: {result.get('error_type')}")
    
    # Test ML speed if available
    client = OllamaClient()
    if client.is_available():
        print("\n🤖 ML analysis speed:")
        start = time.time()
        suggestion = client.analyze_error(error)
        elapsed = time.time() - start
        print(f"  Time: {elapsed*1000:.2f}ms")
        if suggestion:
            print(f"  Response: {suggestion[:100]}...")


def run_all_examples():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 10 + "CommandPro ML (Ollama Integration) Examples" + " " * 16 + "║")
    print("╚" + "=" * 68 + "╝")
    
    example_1_ollama_check()
    example_2_ml_vs_rule_based()
    example_3_command_execution()
    example_4_ml_analysis_with_fallback()
    example_5_streaming()
    example_6_configuration()
    example_7_performance()
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_examples()
