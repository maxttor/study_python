#Task description: https://stepik.org/lesson/24473/step/4
import json

list = json.loads(input())
children = {}
counts = {i['name']: set() for i in list}
classes = [i['name'] for i in list]
classes.sort()


def add_children(root_name, parent_name):
    for child in children[parent_name]:
        counts[root_name].add(child)
        add_children(root_name, child)


for item in list:
    children.setdefault(item['name'], set())
    for parent in item['parents']:
        children.setdefault(parent, set())
        children[parent].add(item['name'])

for item in classes:
    add_children(item, item)
    print(item, ':', str(len(counts[item]) + 1))