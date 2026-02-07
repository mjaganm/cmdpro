"""Error analyzer for parsing and matching error messages"""

from knowledge_base import find_error_type


class ErrorAnalyzer:
    """Analyzes error messages and provides solutions"""
    
    @staticmethod
    def analyze(error_message: str) -> dict:
        """
        Analyze an error message and return solutions
        
        Args:
            error_message: The error message to analyze
            
        Returns:
            Dictionary with analysis results
        """
        if not error_message or not error_message.strip():
            return {
                "success": False,
                "error": "Empty error message provided",
                "error_type": None,
                "solutions": []
            }
        
        error_type = find_error_type(error_message)
        
        if error_type:
            return {
                "success": True,
                "error_type": error_type["name"],
                "solutions": error_type.get("solutions", []),
                "examples": error_type.get("examples", []),
                "original_message": error_message
            }
        else:
            return {
                "success": False,
                "error": "Could not identify error type",
                "error_type": None,
                "original_message": error_message,
                "solutions": [
                    "Try searching online for this error message",
                    "Check the official documentation for the command",
                    "Verify your inputs and try with --help flag",
                ]
            }
