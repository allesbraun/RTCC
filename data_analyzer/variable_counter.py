import javalang


def count_variables(content):
    try:
        tree = javalang.parse.parse(content)
        count = 0
        count += sum(1 for _ in tree.filter(javalang.tree.VariableDeclaration))

        return count 
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")