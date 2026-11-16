"""Standalone regression test: t05 missing bytes and repeat visitor."""

from helpers import AnalyzerTestCase, expected, log


class TestT05MissingBytesAndRepeatVisitor(AnalyzerTestCase):
    def test_t05_missing_bytes_and_repeat_visitor(self):
            source = "\n".join([
                log("2001:db8::7", target="/health", status=204, size="-"),
                log("2001:db8::7", target="/oops", status=503, size=25),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(2, 1, 1, 50.0, 25,
                                      status={"204": 1, "503": 1},
                                      paths=[("/health", 1), ("/oops", 1)]))
