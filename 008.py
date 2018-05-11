#Task description: https://stepik.org/lesson/24474/step/4
from xml.etree import ElementTree

root = ElementTree.fromstring(input())

colors = {'red': 0, 'green': 0, 'blue': 0}

def calc_score(element, score = 1):
    colors[element.attrib['color']] += score
    for child in element:
        calc_score(child, score + 1)

calc_score(root, 1)

print(colors['red'], colors['green'], colors['blue'])