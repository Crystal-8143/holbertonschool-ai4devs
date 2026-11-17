"""Create a fresh report containing the provided event labels."""

def build_report(events, report=[]):
    for event in events:
        if not isinstance(event, str):
            raise ValueError("Event must be a string")
        report.append(event.strip())
    return report

def main():
    morning = ["started", "completed"]
    evening = ["failed"]

    first_report = build_report(morning)
    second_report = build_report(evening)
    print("Morning Report:", first_report)
    print("Evening Report:", second_report)

if __name__ == "__main__":
    main()