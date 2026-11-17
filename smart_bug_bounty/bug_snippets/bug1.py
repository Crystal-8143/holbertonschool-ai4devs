"""Return the last N activity entries, preserving their original order"""

def last_activities(activities, count):
    if not isinstance(count, int):
        raise TypeError("Count must be an integer")
    if count < 0:
        raise ValueError("Count must be a non-negative integer")
    if count == 0:
        return []

    start = max(0, len(activities) - count + 1)
    return activities[start:]

def main():
    history = ["Login", "Search", "View Profile", "Logout"]
    print("Last 2 activities:", last_activities(history, 2))

if __name__ == "__main__":
    main()