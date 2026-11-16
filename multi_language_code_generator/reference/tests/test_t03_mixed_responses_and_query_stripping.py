"""Standalone regression test: t03 mixed responses and query stripping."""

from helpers import AnalyzerTestCase, expected, log


class TestT03MixedResponsesAndQueryStripping(AnalyzerTestCase):
    def test_t03_mixed_responses_and_query_stripping(self):
            source = "\n".join([
                log("203.0.113.10", target="/home", size=512),
                log("203.0.113.11", target="/home?ref=ad", status=404, size=100),
                log("203.0.113.10", method="POST", target="/api/items", status=500, size=0),
                log("203.0.113.12", target="/api/items", status=302, size=40),
            ])
            self.assertEqual(self.analyzer.analyze(source),
                             expected(4, 3, 2, 50.0, 652, status={
                                 "200": 1, "302": 1, "404": 1, "500": 1},
                                      paths=[("/api/items", 2), ("/home", 2)]))
