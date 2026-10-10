"""Numeric display smoke test for the local report workflow."""

import unittest

from tools.numeric_display import verify_numeric_display


class NumericDisplaySmokeTest(unittest.TestCase):
    def test_numeric_reference_display(self):
        self.assertEqual(verify_numeric_display(), 0)


if __name__ == "__main__":
    unittest.main()
