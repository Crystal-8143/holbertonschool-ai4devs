def find_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            return user["name"]

    return user["name"]

users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

name = find_user(users, 5)

print("User:", name)