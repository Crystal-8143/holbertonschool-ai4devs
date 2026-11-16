"""Standalone regression test: lone cr is invalid not silently trimmed."""

from helpers import AnalyzerTestCase, expected, log


class TestLoneCrIsInvalidNotSilentlyTrimmed(AnalyzerTestCase):
    def test_lone_cr_is_invalid_not_silently_trimmed(self):
            source = log(target="/good") + "\n" + log(target="/bad") + "\r"
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=1, malformed=1,
                                      status={"200": 1}, paths=[("/good", 1)]))
