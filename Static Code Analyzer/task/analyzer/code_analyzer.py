# write your code here
import re, os, sys, ast
from pathlib import Path


###### STAGE 1

# In this stage, your program should read Python code from a specified file and
# perform a single check: the length of code lines should not exceed 79 characters.
# characters

# path = input()
# code = 'S001'
# message = 'Too long'
#
#
# with open(path) as file:
#     data = file.readlines()
#     for x, line in enumerate(data, start=1):
#         if len(line) > 79:
#             print(f'Line {x}: {code} {message}')
#         else:
#             x += 1


############ STAGE 2

# Let's add a few more checks to the program. All of them are consistent with
# the PEP8 style guide

############# STAGE 3: Analyze multi-file projects

# In this stage, you need to improve your program so that it can analyze all
# Python files inside a specified directory.

path = ''

if len(sys.argv) > 1 :
    path = sys.argv[1]
else:
    path = sys.argv()
# print('This is it', path)

codes = {'S001':'Too long',
         'S002':'Indentation is not a multiple of four',
         'S003':'Unnecessary semicolon',
         'S004':'At least two spaces required before inline comments',
         'S005':'TODO found',
         'S006':'More than two blank lines used before this line',
         'S007':'Too many spaces after construction_name (def or class)',
         'S008':'Class name class_name should be written in CamelCase',
         'S009':'Function name function_name should be written in snake_case',
         'S010': 'Argument name arg_name should be written in snake_case',
         'S011': 'Variable var_name should be written in snake_case',
         'S012': 'The default argument value is mutable'
         }


def first_code(path, x,line, codes):
    if len(line) > 79:
        code = 'S001'
        print(f'{path}: Line {x}: {code} {codes[code]}')


def second_code(path, x, line, codes):
    if (len(line) - len(line.lstrip())) % 4 != 0 and (len(line) != len(line.lstrip()) != 0):
        code = 'S002'
        print(f'{path}: Line {x}: {code} {codes[code]}')


def third_code(path, x, line, codes):
    if ';' in line:
        if (('#' in line) and (line.index('#')) > (line.index(';'))) \
                or ('#' not in line) \
                and not re.search(r"'.+;.*'", line):
            code = 'S003'
            print(f'{path}: Line {x}: {code} {codes[code]}')


def fourth_code(path, x, line, codes):
    if ('#' in line) and line.index('#') > 0:
        sharpIndex = line.index('#')
        slice = line[:sharpIndex]
        if (len(slice) - len(slice.rstrip())) < 2:
            code = 'S004'
            print(f'{path}: Line {x}: {code} {codes[code]}')


def fifth_code(path, x, line, codes):
    if re.search('TODO', line, re.IGNORECASE):
        if('#' in line):
            result = re.search('TODO', line, re.IGNORECASE)
            if (line.index(result.group()) > line.index('#')):
                code = 'S005'
                print(f'{path}: Line {x}: {code} {codes[code]}')


def code07(path, x, line, codes):
    if re.search('class', line):
        class_end = line.index('class') + 5
        slice1 = line[class_end:]
        if (len(slice1) - len(slice1.lstrip())) > 1:
            code = list(codes)[6]
            print(f'{path}: Line {x}: {code} {codes[code]}')


def code08(path, x, line, codes):
    if re.search('class', line):
        class_end = line.index('class') + 5
        class_name = line[class_end:].lstrip()
        # pattern = r'([A-Z][a-z0-9]+){2,}'
        pattern = r' *([A-Z]+[a-z]+)+'
        if not re.match(pattern, class_name):
            code = list(codes)[7]
            print(f'{path}: Line {x}: {code} {codes[code]}')


def code09(path, x, line, codes):
    if re.search('def', line):
        function_end = line.index('def') + 3
        function_name = line[function_end:].lstrip()
        pattern2 = r'^([a-z_]+)'
        if not re.match(pattern2, function_name):
            code = list(codes)[8]
            print(f'{path}: Line {x}: {code} {codes[code]}')

def code10(tree, path, codes):
    # script = open(path).read()
    # tree = ast.parse(script)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            # print(function_name)
            args = [a.arg for a in node.args.args]
            # print(function_name)
            # print(args)
            pattern2 = r'^([a-z_]+)'
            if args != []:
                for i in args:
                    if not re.match(pattern2, i):
                        code = list(codes)[9]
                        print(f'{path}: Line {node.lineno}: {code} {codes[code]}')


def code11(tree, path, codes):
    # script = open(path).read()
    # tree = ast.parse(script)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            variable_name = node.id
            snakeCase = r'^([a-z_]+)'
            if not re.match(snakeCase, variable_name):
                code = list(codes)[10]
                print(f'{path}: Line {node.lineno}: {code} {codes[code]}')


def code12(tree, path, codes):
    # script = open(path).read()
    # tree = ast.parse(script)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            for item in node.args.defaults:
                if isinstance(item, ast.List):
                    code = list(codes)[11]
                    print(f'{path}: Line {node.lineno}: {code} {codes[code]}')




def code_check(path_name):
    # split_up = path_and_name.split('/')
    # path_name = split_up[-1]
    # print(path_name)
    with open(path_name) as file:
        # tree = ast.parse(file.read(), filename=path_name)
        data = file.readlines()
        blank_line_count = 0
        code = ''
        for x, line in enumerate(data, start=1):
            first_code(path_name, x, line, codes)
            second_code(path_name, x, line, codes)
            third_code(path_name, x, line, codes)
            fourth_code(path_name, x, line, codes)
            fifth_code(path_name, x, line, codes)
            code07(path_name, x, line, codes)
            code08(path_name, x, line, codes)
            code09(path_name, x, line, codes)
            # code10(path_name, line, codes)
            # code11(path_name, line, codes)
            # code12(path_name, line, codes)

            if not line.strip():
                blank_line_count += 1
                if blank_line_count > 2:
                    code = 'S006'
                    print(f'{path_name}: Line {x+1}: {code} {codes[code]}')
                    blank_line_count = 0

            else:
                blank_line_count = 0
                x += 1



def code_check2(path_name):
    with open(path_name) as file:
        tree = ast.parse(file.read())
        code10(tree, path_name, codes)
        code11(tree, path_name, codes)
        code12(tree, path_name, codes)


def file_finder(folder_directory):
    files_list = []
    # with os.scandir(folder_directory) as entries:
    #     for entry in entries:
    #         if entry.isfile() and entry.endswith('.py'):
    #             files.append(entry)
    #         elif entry.dir():
    #             file_finder(entry)
    # return files
    for folderName, subfolders, filenames in os.walk(folder_directory):
        for filename in filenames:
            if filename.endswith('.py') and filename != "tests.py":
                files_list.append(folderName + os.sep + filename)
    return files_list



if path.endswith('.py'):
    code_check(path)
    code_check2(path)
else:
    multiple_paths = file_finder(path)
    multiple_paths.sort()
    # print(multiple_paths)
    for specified_path in multiple_paths:
        # real_path = Path(specified_path)
        # if os.path.isdir(real_path):
        code_check(specified_path)
        code_check2(specified_path)
