#!/usr/bin/env python3
"""
CommandPro Examples and Demo

This file demonstrates how to use CommandPro programmatically
in your own Python projects.
"""

from analyzer import ErrorAnalyzer
from knowledge_base import find_error_type, get_all_patterns


def example_1_basic_usage():
    """Example 1: Basic error analysis"""
    print("=" * 70)
    print("Example 1: Basic Error Analysis")
    print("=" * 70)
    
    error = "command not found: python3"
    print(f"\nAnalyzing error: '{error}'")
    
    result = ErrorAnalyzer.analyze(error)
    print(f"\nResult:")
    print(f"  Success: {result['success']}")
    print(f"  Error Type: {result['error_type']}")
    print(f"  Solutions: {result['solutions']}")


def example_2_programmatic_usage():
    """Example 2: Using in Python code"""
    print("\n\n" + "=" * 70)
    print("Example 2: Programmatic Usage in Python Code")
    print("=" * 70)
    
    errors_to_test = [
        "ModuleNotFoundError: No module named requests",
        "Access is denied",
        "Connection timeout",
    ]
    
    for error in errors_to_test:
        result = ErrorAnalyzer.analyze(error)
        if result['success']:
            print(f"\n✓ {result['error_type']}")
            print(f"  First solution: {result['solutions'][0]}")
        else:
            print(f"\n✗ Could not identify: {error}")


def example_3_knowledge_base():
    """Example 3: Exploring the knowledge base"""
    print("\n\n" + "=" * 70)
    print("Example 3: Exploring Knowledge Base")
    print("=" * 70)
    
    patterns = get_all_patterns()
    print(f"\nTotal error types: {len(patterns)}\n")
    
    for pattern in patterns:
        print(f"  • {pattern['name']}")
        print(f"    Patterns: {len(pattern['patterns'])}")
        print(f"    Solutions: {len(pattern['solutions'])}")
        print()


def example_4_error_detection():
    """Example 4: Finding error types"""
    print("\n\n" + "=" * 70)
    print("Example 4: Direct Error Type Detection")
    print("=" * 70)
    
    messages = [
        "Address already in use: port 8000",
        "UNKNOWN ERROR TYPE XYZ",
    ]
    
    for msg in messages:
        error_type = find_error_type(msg)
        if error_type:
            print(f"\n✓ '{msg}'")
            print(f"  → Matched: {error_type['name']}")
        else:
            print(f"\n✗ '{msg}'")
            print(f"  → No match found")


def example_5_batch_processing():
    """Example 5: Processing multiple errors"""
    print("\n\n" + "=" * 70)
    print("Example 5: Batch Processing Errors")
    print("=" * 70)
    
    error_log = [
        "2024-01-15 10:23:45 - Command not found: npm",
        "2024-01-15 10:24:12 - Cannot find the path specified",
        "2024-01-15 10:25:33 - ModuleNotFoundError: No module named 'numpy'",
        "2024-01-15 10:26:01 - Permission denied",
    ]
    
    print("\nProcessing error log...")
    identified = 0
    unidentified = 0
    
    for log_line in error_log:
        # Extract error message (simple parsing)
        error_msg = log_line.split(" - ", 1)[1]
        result = ErrorAnalyzer.analyze(error_msg)
        
        if result['success']:
            print(f"✓ {result['error_type']}")
            identified += 1
        else:
            print(f"✗ {error_msg}")
            unidentified += 1
    
    print(f"\nSummary: {identified} identified, {unidentified} unidentified")


def example_6_custom_integration():
    """Example 6: Creating a wrapper for custom integration"""
    print("\n\n" + "=" * 70)
    print("Example 6: Custom Integration Wrapper")
    print("=" * 70)
    
    class ErrorHelper:
        """Custom error helper class"""
        
        @staticmethod
        def quick_fix(error_message):
            """Get the most important solution"""
            result = ErrorAnalyzer.analyze(error_message)
            if result['success'] and result['solutions']:
                return result['solutions'][0]
            return "Try searching online for this error"
        
        @staticmethod
        def get_example(error_message):
            """Get an example command"""
            result = ErrorAnalyzer.analyze(error_message)
            if result['success'] and result['examples']:
                return result['examples'][0]
            return None
    
    # Usage
    error = "ModuleNotFoundError: no module named requests"
    print(f"\nError: {error}")
    print(f"Quick fix: {ErrorHelper.quick_fix(error)}")
    print(f"Example: {ErrorHelper.get_example(error)}")


def example_7_confidence_scoring():
    """Example 7: Pattern confidence analysis"""
    print("\n\n" + "=" * 70)
    print("Example 7: Error Type Analysis")
    print("=" * 70)
    
    test_cases = [
        ("ModuleNotFoundError: No module named 'sys'", "Should match Module error"),
        ("port already in use", "Should match Port error"),
        ("xyz abc def", "Should not match any pattern"),
    ]
    
    for error_msg, description in test_cases:
        result = ErrorAnalyzer.analyze(error_msg)
        status = "✓" if result['success'] else "✗"
        error_type = result.get('error_type', 'Unknown')
        print(f"{status} {description}")
        print(f"   Input: '{error_msg}'")
        print(f"   Result: {error_type}\n")


def run_all_examples():
    """Run all examples"""
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "CommandPro Examples & Demo" + " " * 26 + "║")
    print("╚" + "=" * 68 + "╝")
    
    example_1_basic_usage()
    example_2_programmatic_usage()
    example_3_knowledge_base()
    example_4_error_detection()
    example_5_batch_processing()
    example_6_custom_integration()
    example_7_confidence_scoring()
    
    print("\n" + "=" * 70)
    print("Examples completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    run_all_examples()
