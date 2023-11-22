import javalang


def count_recursive(content):
    try:
        tree = javalang.parse.parse(content)
        num_recursion = 0

        for _, node in tree.filter(javalang.tree.MethodDeclaration):

            temp_name = node.name
            if node.name+',' in str(node).replace('name=' + temp_name, ''):
                num_recursion = str(node).replace('name=' + temp_name, '').count(node.name+',')
        
        return num_recursion
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")


