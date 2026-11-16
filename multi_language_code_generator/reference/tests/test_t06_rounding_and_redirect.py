"""Standalone regression test: t06 rounding and redirect."""

from helpers import AnalyzerTestCase, expected, log


class TestT06RoundingAndRedirect(AnalyzerTestCase):
    def test_t06_rounding_and_redirect(self):
            source = "\n".join([
                log("192.0.2.1", target="/x", status=301, size=3),
                log("192.0.2.2", target="/x?search=a", status=499, size=4),
                log("192.0.2.3", target="/y", status=599, size=4),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(3, 3, 2, 66.67, 11,
                                      status={"301": 1, "499": 1, "599": 1},
                                      paths=[("/x", 2), ("/y", 1)]))
