"""Standalone regression test: t04 malformed entry is ignored."""

from helpers import AnalyzerTestCase, expected, log


class TestT04MalformedEntryIsIgnored(AnalyzerTestCase):
    def test_t04_malformed_entry_is_ignored(self):
            source = log("198.51.100.7", target="/ok", size=10) + "\nnot an HTTP log record"
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=10, malformed=1,
                                      status={"200": 1}, paths=[("/ok", 1)]))
