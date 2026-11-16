"""Standalone regression test: non ascii or invalid request targets."""

from helpers import AnalyzerTestCase, expected, log


class TestNonAsciiOrInvalidRequestTargets(AnalyzerTestCase):
    def test_non_ascii_or_invalid_request_targets(self):
            source = "\n".join([
                log(target="/café"), log(target="not/a/path"),
                log(target='/bad"quote'), log(target="/bad path"),
                log(target="/ok?x=1?y=2"),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=1, malformed=4,
                                      status={"200": 1}, paths=[("/ok", 1)]))
