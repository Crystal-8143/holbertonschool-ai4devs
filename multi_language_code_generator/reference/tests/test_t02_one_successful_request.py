"""Standalone regression test: t02 one successful request."""

from helpers import AnalyzerTestCase, expected, log


class TestT02OneSuccessfulRequest(AnalyzerTestCase):
    def test_t02_one_successful_request(self):
            source = log("203.0.113.10", target="/home", size=512)
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=512, status={"200": 1},
                                      paths=[("/home", 1)]))
