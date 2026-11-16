"""Standalone regression test: t08 invalid status bytes and method."""

from helpers import AnalyzerTestCase, expected, log


class TestT08InvalidStatusBytesAndMethod(AnalyzerTestCase):
    def test_t08_invalid_status_bytes_and_method(self):
            source = "\n".join([
                log("192.0.2.8", target="/valid", size=9),
                log("192.0.2.8", target="/bad-status", status=700),
                log("192.0.2.8", target="/bad-bytes", size=-1),
                log("192.0.2.8", method="get", target="/bad-method"),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=9, malformed=3,
                                      status={"200": 1}, paths=[("/valid", 1)]))
