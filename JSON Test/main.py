import json

with open('data.json', 'r') as f:
    users = json.load(f)


name = input('name: ')
command = input('command: ')

if name not in users:
    users[name] = {}
    users[name]['Level'] = 0

with open('data.json', 'w') as f:
    json.dump(users, f)


if command not ' ':
    with open('data.json', 'r') as f:
        users = json.load(f)

    if command in users:
        print(users)
