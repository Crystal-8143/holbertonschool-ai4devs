"""Standalone regression test: t09 blank line and trailing lf."""

from helpers import AnalyzerTestCase, expected, log


class TestT09BlankLineAndTrailingLf(AnalyzerTestCase):
    def test_t09_blank_line_and_trailing_lf(self):
            source = log("198.51.100.20", target="/ok") + "\n\n"
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=1, malformed=1,
                                      status={"200": 1}, paths=[("/ok", 1)]))
