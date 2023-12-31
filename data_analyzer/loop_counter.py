import javalang
from javalang.ast import Node
from javalang.tree import ForStatement, WhileStatement


def count_loops(content):
    try:
        tree = javalang.parse.parse(content)
        count_for = sum(1 for _, node in tree.filter(ForStatement))
        count_while = sum(1 for _, node in tree.filter(WhileStatement))
        return count_for + count_while
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")