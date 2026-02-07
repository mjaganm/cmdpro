"""Command line interface for the error helper"""

import sys
from analyzer import ErrorAnalyzer


def format_solutions(solutions):
    """Format solutions for console output"""
    output = []
    for i, solution in enumerate(solutions, 1):
        output.append(f"  {i}. {solution}")
    return "\n".join(output)


def format_examples(examples):
    """Format examples for console output"""
    output = []
    for i, example in enumerate(examples, 1):
        output.append(f"  {i}. {example}")
    return "\n".join(output)


def print_result(result):
    """Print analysis result in a formatted way"""
    if result["success"]:
        print(f"\n✓ Error Type: {result['error_type']}\n")
        print("Suggested Solutions:")
        print(format_solutions(result["solutions"]))
        
        if result.get("examples"):
            print("\nTry These Examples:")
            print(format_examples(result["examples"]))
        print()
    else:
        print(f"\n✗ {result['error']}\n")
        if result.get("solutions"):
            print("Suggestions:")
            print(format_solutions(result["solutions"]))
        print()


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        # Interactive mode
        print("=" * 60)
        print("CommandPro - Error Helper")
        print("=" * 60)
        print("\nPaste your error message (press Enter twice to submit):\n")
        
        lines = []
        empty_lines = 0
        
        while True:
            try:
                line = input()
                if line == "":
                    empty_lines += 1
                    if empty_lines >= 2:
                        break
                    lines.append(line)
                else:
                    empty_lines = 0
                    lines.append(line)
            except EOFError:
                break
        
        error_message = "\n".join(lines).strip()
        
        if error_message:
            result = ErrorAnalyzer.analyze(error_message)
            print_result(result)
        else:
            print("No error message provided.")
    else:
        # Argument mode
        error_message = " ".join(sys.argv[1:])
        result = ErrorAnalyzer.analyze(error_message)
        print_result(result)


if __name__ == "__main__":
    main()
