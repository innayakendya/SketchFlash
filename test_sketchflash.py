# test_sketchflash.py
"""
Tests for SketchFlash module.
"""

import unittest
from sketchflash import SketchFlash

class TestSketchFlash(unittest.TestCase):
    """Test cases for SketchFlash class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SketchFlash()
        self.assertIsInstance(instance, SketchFlash)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SketchFlash()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
