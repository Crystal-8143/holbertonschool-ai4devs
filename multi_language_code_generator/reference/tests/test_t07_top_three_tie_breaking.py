"""Standalone regression test: t07 top three tie breaking."""

from helpers import AnalyzerTestCase, expected, log


class TestT07TopThreeTieBreaking(AnalyzerTestCase):
    def test_t07_top_three_tie_breaking(self):
            source = "\n".join([log(target=f"/{path}") for path in "cabd"])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(4, 1, size=4, status={"200": 4},
                                      paths=[("/a", 1), ("/b", 1), ("/c", 1)]))
