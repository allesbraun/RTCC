import javalang


def count_hash_sets(content):
    tree = javalang.parse.parse(content)
    num_hash_sets = 0

    for _, node in tree.filter(javalang.tree.ClassDeclaration):
        for path, node in node:
            if isinstance(node, javalang.tree.ClassCreator):
                if 'HashSet' in node.type.name:
                    num_hash_sets += 1

    return num_hash_sets