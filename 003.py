#Task description: https://stepik.org/lesson/24463/step/7
exceptions = [input().split() for i in range(int(input()))]
queries = [input() for i in range(int(input()))]
dict = {item[0]: item[2:] for item in exceptions}
stack = []

def check(name):
    for item in dict[name]:
        if item in stack:
            return False
        elif not check(item):
            return False
    return True

for item in queries:
    if not check(item):
        print(item)
    stack.append(item)