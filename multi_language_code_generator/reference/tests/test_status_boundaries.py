"""Standalone regression test: status boundaries."""

from helpers import AnalyzerTestCase, expected, log


class TestStatusBoundaries(AnalyzerTestCase):
    def test_status_boundaries(self):
            source = "\n".join([
                log(target="/a", status=100), log(target="/b", status=399),
                log(target="/c", status=400), log(target="/d", status=599),
                log(status=99), log(status=600),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(4, 1, 2, 50.0, 4, malformed=2,
                                      status={"100": 1, "399": 1, "400": 1, "599": 1},
                                      paths=[("/a", 1), ("/b", 1), ("/c", 1)]))
