"""Standalone regression test: round half up at exact tie."""

from helpers import AnalyzerTestCase, expected, log


class TestRoundHalfUpAtExactTie(AnalyzerTestCase):
    def test_round_half_up_at_exact_tie(self):
            # 1 error out of 32 requests = 3.125%; half-up means 3.13%, not 3.12%.
            source = "\n".join([log(status=400)] + [log() for _ in range(31)])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(32, 1, 1, 3.13, 32,
                                      status={"200": 31, "400": 1}, paths=[("/", 32)]))
