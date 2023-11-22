import javalang
from javalang.tree import MethodInvocation


def count_sorts(content):
    try:
        tree = javalang.parse.parse(content)
        count = sum(1 for _, node in tree.filter(MethodInvocation) if node.member == 'sort')
        return count
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")