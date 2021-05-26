import os


# Написать утилиту командной строки, формирующую дерево каталогов и файлов с учетом вложенности и начиная с заданного
# пути. Результат должен быть выдан в виде текста в формате graphviz.
def recursive_directories():
    for dir_path, dir_names, filenames in os.walk(os.getcwd()):
        print("Files->")
        # перебор файлов
        for filename in filenames:
            print('  ' + os.path.basename(dir_path) + " -> " + f'"{filename}"')
        print("Directories->")
        for dirname in dir_names:
            print('  ' + os.path.basename(dir_path) + " -> " + dirname)


def tree_graph_print(s):
    if s == 'start':
        print('digraph G {')
    elif s == 'end':
        print('}')
    return s


def build_tree():
    tree_graph_print('start')
    recursive_directories()
    tree_graph_print('end')


if __name__ == '__main__':
    build_tree()
