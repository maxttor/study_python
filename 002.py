#Task description: https://stepik.org/lesson/24462/step/7
classes = [input().split() for i in range(int(input()))]
queries = [input().split() for i in range(int(input()))]
dict = {item[0]: item[2:] for item in classes}

def is_parent(class1, class2):
    if class1 in dict[class2]:
        return 'Yes'
    elif class1 == class2:
        return 'Yes'
    else:
        result = 'No'
        for item in dict[class2]:
            result = is_parent(class1, item)
            if result == 'Yes':
                return result
        return result

for item in queries:
    print(is_parent(item[0], item[1]))