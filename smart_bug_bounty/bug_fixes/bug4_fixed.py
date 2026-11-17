"""Create a fresh report containing the provided event labels."""


def build_report(events, report=None):
    # A new list must be created per call when one isn't supplied.
    if report is None:
        report = []
    for event in events:
        if not isinstance(event, str):
            raise TypeError("event labels must be strings")
        report.append(event.strip())
    return report


def main():
    morning = ["started", "completed"]
    evening = ["failed"]

    first_report = build_report(morning)
    second_report = build_report(evening)
    print("Morning report:", first_report)
    print("Evening report:", second_report)


if __name__ == "__main__":
    main()
