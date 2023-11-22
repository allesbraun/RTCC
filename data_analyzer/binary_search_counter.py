import javalang


def count_binSearch(content):
    try:
        tree = javalang.parse.parse(content)
        currently_analyzed_methods = set()
        count = 0
        for _, node in tree.filter(javalang.tree.MethodInvocation):
            if node.member == 'binarySearch':
                if node.member in currently_analyzed_methods:
                    continue  # Skip this occurrence, it's a recursive call
                else:
                    currently_analyzed_methods.add(node.member)
                    count += 1
        return count
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")