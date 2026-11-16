"""Standalone regression test: t01 empty input."""

from helpers import AnalyzerTestCase, expected, log


class TestT01EmptyInput(AnalyzerTestCase):
    def test_t01_empty_input(self):
            self.assertEqual(self.analyzer.analyze(""), expected())
