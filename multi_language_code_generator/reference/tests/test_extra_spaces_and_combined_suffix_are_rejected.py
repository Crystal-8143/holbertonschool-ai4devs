"""Standalone regression test: extra spaces and combined suffix are rejected."""

from helpers import AnalyzerTestCase, expected, log


class TestExtraSpacesAndCombinedSuffixAreRejected(AnalyzerTestCase):
    def test_extra_spaces_and_combined_suffix_are_rejected(self):
            source = "\n".join([
                " " + log(), log() + " ", log().replace(" - - ", "  - - "),
                log() + ' "-" "Mozilla/5.0"', log(target="/valid"),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(1, 1, size=1, malformed=4,
                                      status={"200": 1}, paths=[("/valid", 1)]))
