"""Standalone regression test: crlf and single terminating newline."""

from helpers import AnalyzerTestCase, expected, log


class TestCrlfAndSingleTerminatingNewline(AnalyzerTestCase):
    def test_crlf_and_single_terminating_newline(self):
            source = log(target="/first") + "\r\n" + log(target="/second") + "\r\n"
            self.assertEqual(self.analyzer.analyze(source),
                             expected(2, 1, size=2, status={"200": 2},
                                      paths=[("/first", 1), ("/second", 1)]))
