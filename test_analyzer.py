#!/usr/bin/env python3
"""Test script for CommandPro error analyzer"""

from analyzer import ErrorAnalyzer

def test_error_analyzer():
    """Test various error messages"""
    
    test_cases = [
        "command not found: python3",
        "No such file or directory: /path/to/file",
        "Access is denied",
        "Address already in use: port 8000",
        "ModuleNotFoundError: No module named 'requests'",
        "Connection timeout",
        "authentication failed",
        "SyntaxError: unexpected token",
        "disk full",
        "unrecognized arguments",
    ]
    
    print("=" * 70)
    print("CommandPro Error Analyzer - Test Suite")
    print("=" * 70)
    
    for i, error_msg in enumerate(test_cases, 1):
        print(f"\n[Test {i}] Testing: '{error_msg}'")
        print("-" * 70)
        
        result = ErrorAnalyzer.analyze(error_msg)
        
        if result["success"]:
            print(f"✓ Error Type: {result['error_type']}")
            print(f"\nSolutions:")
            for j, sol in enumerate(result["solutions"], 1):
                print(f"  {j}. {sol}")
            
            if result.get("examples"):
                print(f"\nExamples:")
                for j, ex in enumerate(result["examples"], 1):
                    print(f"  {j}. {ex}")
        else:
            print(f"✗ {result['error']}")
            print(f"\nSuggestions:")
            for j, sol in enumerate(result["solutions"], 1):
                print(f"  {j}. {sol}")
    
    print("\n" + "=" * 70)
    print("All tests completed!")
    print("=" * 70)


if __name__ == "__main__":
    test_error_analyzer()
