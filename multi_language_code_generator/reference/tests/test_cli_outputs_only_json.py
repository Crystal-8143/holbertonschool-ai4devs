"""Standalone regression test: cli outputs only json."""

from helpers import AnalyzerTestCase, expected, log
import subprocess
import json
import sys
from pathlib import Path


class TestCliOutputsOnlyJson(AnalyzerTestCase):
    def test_cli_outputs_only_json(self):
            script = Path(__file__).resolve().parents[1] / "log_analyzer.py"
            source = log(target="/cli", size=7) + "\n"
            run = subprocess.run(
                [sys.executable, str(script)], input=source,
                text=True, capture_output=True, check=True,
            )
            self.assertEqual(run.stderr, "")
            self.assertEqual(json.loads(run.stdout),
                             expected(1, 1, size=7, status={"200": 1},
                                      paths=[("/cli", 1)]))
