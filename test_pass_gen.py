import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest, string
from pass_gen import generate
class T(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(generate(20)), 20)
    def test_charset(self):
        allowed = set(string.ascii_letters + string.digits + "!@#$%^&*")
        self.assertTrue(set(generate(50)) <= allowed)
    def test_too_short(self):
        with self.assertRaises(ValueError): generate(4)
if __name__ == "__main__": unittest.main()
