"""Standalone regression test: case sensitive visitors and paths."""

from helpers import AnalyzerTestCase, expected, log


class TestCaseSensitiveVisitorsAndPaths(AnalyzerTestCase):
    def test_case_sensitive_visitors_and_paths(self):
            source = "\n".join([
                log("CLIENT", target="/A"), log("client", target="/a"),
                log("CLIENT", target="/A?x=1"), log("CLIENT", target="/A/"),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(4, 2, size=4, status={"200": 4},
                                      paths=[("/A", 2), ("/A/", 1), ("/a", 1)]))
