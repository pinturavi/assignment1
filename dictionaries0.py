from inputs import get_int, get_string

n = get_int()

employees = []

for i in range(n):
    name = get_string("Enter a name > ")

    experience = get_int("Enter experience > ")

    employees.append({'name': name, 'experience': experience})


for e in employees:
    print(f"name : {e['name']}")
    print(f"experience : {e['experience']}")