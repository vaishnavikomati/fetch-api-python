import requests

# Fetch data from API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

# Parse JSON response
data = response.json()

print("User List:")
for user in data:
    print(f"{user['id']} - {user['name']}")

# Search / Filter
search = input("\nEnter name to search: ").lower()

print("\nSearch Results:")
found = False

for user in data:
    if search in user['name'].lower():
        print(f"ID: {user['id']}")
        print(f"Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City: {user['address']['city']}")
        print("-" * 20)
        found = True

if not found:
    print("No user found")