"""Return the last N activity entries, preserving their original order."""


def last_activities(activities, count):
    if not isinstance(count, int):
        raise TypeError("count must be an integer")
    if count < 0:
        raise ValueError("count must be non-negative")
    if count == 0:
        return []

    # Start at exactly len(activities) - count (not one position later).
    start = max(0, len(activities) - count)
    return activities[start:]


def main():
    history = ["login", "search", "view", "logout"]
    print("Last two activities:", last_activities(history, 2))


if __name__ == "__main__":
    main()
