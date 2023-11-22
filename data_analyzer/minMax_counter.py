
import javalang


def count_minMax(content):
    try:
        tree = javalang.parse.parse(content)

        min_calls = 0
        max_calls = 0

        for path, node in tree:
            if isinstance(node, javalang.tree.MethodInvocation):
                method_name = node.member
                if method_name == "min":
                    min_calls += 1
                elif method_name == "max":
                    max_calls += 1

        return min_calls + max_calls
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")