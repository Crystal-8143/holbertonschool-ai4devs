"""Standalone regression test: empty line is malformed."""

from helpers import AnalyzerTestCase, expected, log


class TestEmptyLineIsMalformed(AnalyzerTestCase):
    def test_empty_line_is_malformed(self):
            self.assertEqual(self.analyzer.analyze("\n"), expected(malformed=1))
            self.assertEqual(self.analyzer.analyze("\n\n"), expected(malformed=2))
