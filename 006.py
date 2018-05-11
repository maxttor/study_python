#Task description: https://stepik.org/lesson/24471/step/7
import re
import requests

a = input()
text = requests.get(a).text
links = re.findall(r"<a.+?href=[\"'](?:(?:(?:http|ftp)(?:s)?://)|)([^\"/:']+\.\w+).*?[\"']", text)
links = list(set(links))
links.sort()
print(*links, sep='\n')