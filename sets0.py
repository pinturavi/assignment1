
from inputs import get_int, get_string

names = set()

n = get_int()

for i in range(n):
    name = get_string("Enter a name > ")
    names.add(name)

print(names)

if "ravi" in names:
    print("names contains ravi")