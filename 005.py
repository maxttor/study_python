#Task description: https://stepik.org/lesson/24471/step/6
import re
import requests

a = input()
b = input()


def spider(a, b, depth=0):
    result = requests.get(a)
    if result.status_code != 200:
        return False
    else:
        links = re.findall(r"<a.+href=\"(.+)\">", result.text)
        for link in links:
            if link == b and depth == 1:
                return True
            elif depth < 2:
                if spider(link, b, depth + 1):
                    return True
        return False


if spider(a, b):
    print('Yes')
else:
    print('No')