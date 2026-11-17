"""Run from repository root: python3 -m unittest discover -s smart_bug_bounty/bug_fixes/tests -p 'test_*.py' -v"""
import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_python(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


last_activities = load_python("bug1_fixed").last_activities
build_report = load_python("bug4_fixed").build_report


class TestBug1(unittest.TestCase):
    def test_two_recent(self):
        self.assertEqual(last_activities(["login", "search", "view", "logout"], 2), ["view", "logout"])

    def test_zero_count(self):
        self.assertEqual(last_activities(["a", "b"], 0), [])

    def test_more_than_length(self):
        self.assertEqual(last_activities(["a", "b"], 5), ["a", "b"])

    def test_empty_list(self):
        self.assertEqual(last_activities([], 3), [])

    def test_one_recent(self):
        self.assertEqual(last_activities(["a", "b"], 1), ["b"])

    def test_negative_rejected(self):
        with self.assertRaises(ValueError):
            last_activities(["a"], -1)

    def test_noninteger_rejected(self):
        with self.assertRaises(TypeError):
            last_activities(["a"], 1.5)


class TestBug4(unittest.TestCase):
    def test_calls_are_independent(self):
        morning = build_report(["started", "completed"])
        evening = build_report(["failed"])
        self.assertEqual(morning, ["started", "completed"])
        self.assertEqual(evening, ["failed"])
        self.assertIsNot(morning, evening)

    def test_whitespace_trimmed(self):
        self.assertEqual(build_report(["  login  ", "logout "]), ["login", "logout"])

    def test_existing_report_allowed(self):
        existing = ["earlier"]
        result = build_report([" later "], existing)
        self.assertIs(result, existing)
        self.assertEqual(result, ["earlier", "later"])

    def test_empty_events(self):
        self.assertEqual(build_report([]), [])

    def test_nonstring_rejected(self):
        with self.assertRaises(TypeError):
            build_report([42])

    def test_second_call_does_not_mutate_first(self):
        first = build_report(["a"])
        build_report(["b"])
        self.assertEqual(first, ["a"])


if __name__ == "__main__":
    unittest.main()
