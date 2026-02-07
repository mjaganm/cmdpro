#!/usr/bin/env python3
"""Unit tests for CommandPro"""

import unittest
from analyzer import ErrorAnalyzer
from knowledge_base import find_error_type, get_all_patterns


class TestErrorAnalyzer(unittest.TestCase):
    """Test cases for ErrorAnalyzer"""
    
    def test_command_not_found(self):
        """Test detection of 'command not found' errors"""
        result = ErrorAnalyzer.analyze("command not found: xyz")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Command Not Found")
    
    def test_file_not_found(self):
        """Test detection of 'file not found' errors"""
        result = ErrorAnalyzer.analyze("cannot find the path specified")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "File or Directory Not Found")
    
    def test_permission_denied(self):
        """Test detection of permission errors"""
        result = ErrorAnalyzer.analyze("Access is denied")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Permission Denied")
    
    def test_port_in_use(self):
        """Test detection of port already in use"""
        result = ErrorAnalyzer.analyze("Address already in use: port 8000")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Port Already in Use")
    
    def test_module_not_found(self):
        """Test detection of missing module"""
        result = ErrorAnalyzer.analyze("ModuleNotFoundError: No module named 'requests'")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Module or Package Not Found")
    
    def test_network_error(self):
        """Test detection of network errors"""
        result = ErrorAnalyzer.analyze("Connection timeout")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Network Connection Error")
    
    def test_auth_failed(self):
        """Test detection of authentication failures"""
        result = ErrorAnalyzer.analyze("authentication failed")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Authentication Failed")
    
    def test_syntax_error(self):
        """Test detection of syntax errors"""
        result = ErrorAnalyzer.analyze("SyntaxError: unexpected token")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Syntax Error")
    
    def test_disk_full(self):
        """Test detection of disk full errors"""
        result = ErrorAnalyzer.analyze("no space left on device")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Disk Space Error")
    
    def test_invalid_argument(self):
        """Test detection of invalid argument errors"""
        result = ErrorAnalyzer.analyze("unrecognized arguments")
        self.assertTrue(result["success"])
        self.assertEqual(result["error_type"], "Invalid Argument or Option")
    
    def test_empty_message(self):
        """Test handling of empty error message"""
        result = ErrorAnalyzer.analyze("")
        self.assertFalse(result["success"])
        self.assertIn("Empty", result["error"])
    
    def test_unknown_error(self):
        """Test handling of unknown error type"""
        result = ErrorAnalyzer.analyze("some random error that doesn't match")
        self.assertFalse(result["success"])
        self.assertIn("Could not identify", result["error"])
        self.assertTrue(len(result["solutions"]) > 0)
    
    def test_result_has_solutions(self):
        """Test that successful analysis returns solutions"""
        result = ErrorAnalyzer.analyze("command not found")
        self.assertTrue(result["success"])
        self.assertTrue(len(result["solutions"]) > 0)
    
    def test_result_has_examples(self):
        """Test that successful analysis returns examples"""
        result = ErrorAnalyzer.analyze("ModuleNotFoundError")
        self.assertTrue(result["success"])
        self.assertTrue(len(result["examples"]) > 0)
    
    def test_case_insensitivity(self):
        """Test that error matching is case-insensitive"""
        result1 = ErrorAnalyzer.analyze("command not found")
        result2 = ErrorAnalyzer.analyze("COMMAND NOT FOUND")
        self.assertEqual(result1["error_type"], result2["error_type"])


class TestKnowledgeBase(unittest.TestCase):
    """Test cases for knowledge base"""
    
    def test_patterns_exist(self):
        """Test that patterns are defined"""
        patterns = get_all_patterns()
        self.assertTrue(len(patterns) > 0)
    
    def test_patterns_have_required_fields(self):
        """Test that all patterns have required fields"""
        patterns = get_all_patterns()
        for pattern in patterns:
            self.assertIn("name", pattern)
            self.assertIn("patterns", pattern)
            self.assertIn("solutions", pattern)
            self.assertIn("examples", pattern)
    
    def test_find_error_type(self):
        """Test find_error_type function"""
        error_type = find_error_type("command not found")
        self.assertIsNotNone(error_type)
        self.assertEqual(error_type["name"], "Command Not Found")
    
    def test_find_unknown_error_type(self):
        """Test finding unknown error type"""
        error_type = find_error_type("completely unknown error xyz 123")
        self.assertIsNone(error_type)


if __name__ == "__main__":
    unittest.main(verbosity=2)
