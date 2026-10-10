"""Visual fixture smoke test for the local report workflow."""

import unittest

from tools.render_fixture import render_fixture


class VisualFixtureSmokeTest(unittest.TestCase):
    def test_visual_fixture_renders(self):
        self.assertEqual(render_fixture(), 0)


if __name__ == "__main__":
    unittest.main()
