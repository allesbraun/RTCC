import javalang


def count_methods(content):
    tree = javalang.parse.parse(content)
    count = 0

    for _ in tree.filter(javalang.tree.MethodDeclaration):
        count += 1

    return count