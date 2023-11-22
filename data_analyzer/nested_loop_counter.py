import javalang
from javalang.tree import ForStatement, WhileStatement


def count_nested_loops(content):
    try:
        tree = javalang.parse.parse(content)
        num_nested_loop = 0
        for_statements = tree.filter(ForStatement)
        while_statements = tree.filter(WhileStatement)
        loop_statements = list(for_statements) + list(while_statements)
        for _, node in loop_statements:
            sum = len(list(node.filter(ForStatement))) + len(list(node.filter(WhileStatement)))
            if sum != 1 and sum > num_nested_loop:
                num_nested_loop = sum
        
        return num_nested_loop
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")