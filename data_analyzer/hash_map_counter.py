import javalang


def count_hash_maps(content):
    try:
        tree = javalang.parse.parse(content)
        num_hash_maps = 0

        for _, node in tree.filter(javalang.tree.ClassDeclaration):
            for path, node in node:
                if isinstance(node, javalang.tree.ClassCreator):
                    if 'HashMap' in node.type.name:
                        num_hash_maps += 1

        return num_hash_maps
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")