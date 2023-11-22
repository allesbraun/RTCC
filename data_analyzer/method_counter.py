import javalang


def count_methods(content):
    try:
        tree = javalang.parse.parse(content)
        count = 0

        for _ in tree.filter(javalang.tree.MethodDeclaration):
            count += 1

        return count
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")