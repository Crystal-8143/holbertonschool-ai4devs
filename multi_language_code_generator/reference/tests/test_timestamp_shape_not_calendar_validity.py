"""Standalone regression test: timestamp shape not calendar validity."""

from helpers import AnalyzerTestCase, expected, log


class TestTimestampShapeNotCalendarValidity(AnalyzerTestCase):
    def test_timestamp_shape_not_calendar_validity(self):
            valid_shape = log(timestamp="99/Zzz/0000:99:99:99 -9999")
            bad_shapes = [
                log(timestamp="9/Nov/2026:10:00:00 +1100"),
                log(timestamp="15/November/2026:10:00:00 +1100"),
                log(timestamp="15/Nov/2026:10:00:00 +11:00"),
            ]
            self.assertEqual(self.analyzer.analyze("\n".join([valid_shape] + bad_shapes)),
                             expected(1, 1, size=1, malformed=3,
                                      status={"200": 1}, paths=[("/", 1)]))
