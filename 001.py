#Task description: https://stepik.org/lesson/24460/step/9
commands = [input().split() for i in range(int(input()))]
namespaces = {'global': {'parent': None, 'vars': [], 'children': {}}}

def get_namespace(name, namespace = namespaces['global']):
    if name == 'global':
        return namespace
    else:
        for key, value in namespace['children'].items():
            if key == name:
                return value
            else:
                result = get_namespace(name, value)
                if (result != None):
                    return result

def create_namespace(name, parent):
    namespace = get_namespace(parent)
    if namespace != None:
        namespace['children'][name] = {'parent': parent, 'vars': [], 'children': {}}

def add_var(namespace_name, var_name):
    namespace = get_namespace(namespace_name)
    if namespace != None:
        namespace['vars'].append(var_name)

def get_var(namespace_name, var_name):
    namespace = get_namespace(namespace_name)
    if namespace == None:
        return 'None'
    elif var_name in namespace['vars']:
        return namespace_name
    elif namespace_name == 'global':
        return 'None'
    else:
         return get_var(namespace['parent'], var_name)

for command in commands:
    if command[0] == 'create':
        create_namespace(command[1], command[2])
    elif command[0] == 'add':
        add_var(command[1], command[2])
    elif command[0] == 'get':
        print(get_var(command[1], command[2]))