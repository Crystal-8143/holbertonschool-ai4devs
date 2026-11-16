"""Standalone regression test: byte value limit and large leading zeroes."""

from helpers import AnalyzerTestCase, expected, log, MAX_SAFE_BYTES


class TestByteValueLimitAndLargeLeadingZeroes(AnalyzerTestCase):
    def test_byte_value_limit_and_large_leading_zeroes(self):
            source = "\n".join([
                log(target="/max", size=MAX_SAFE_BYTES),
                log(target="/overflow", size=MAX_SAFE_BYTES + 1),
                log(target="/small", size="00004"),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(2, 1, size=MAX_SAFE_BYTES + 4, malformed=1,
                                      status={"200": 2},
                                      paths=[("/max", 1), ("/small", 1)]))
            self.assertIsNone(self.analyzer.parse_line(log(size="9" * 5000)))
