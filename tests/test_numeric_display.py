"""macOS numeric display smoke test for the local report workflow."""

import subprocess
import sys
import unittest


class NumericDisplaySmokeTest(unittest.TestCase):
    def test_numeric_reference_display_opens(self):
        if sys.platform != "darwin":
            self.skipTest("numeric display smoke test is macOS-only")
        result = subprocess.run(
            ["open", "-a", "Calculator"],
            check=False,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        self.assertEqual(result.returncode, 0)


if __name__ == "__main__":
    unittest.main()
