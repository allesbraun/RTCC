import javalang
from javalang.tree import MethodInvocation


def count_sorts(content):
    tree = javalang.parse.parse(content)
    count = sum(1 for _, node in tree.filter(MethodInvocation) if node.member == 'sort')
    return count

# import javalang

# def count_sorts(content):
#     tree = javalang.parse.parse(content)
#     currently_analyzed_methods = set()
#     count = 0
#     for _, node in tree.filter(javalang.tree.MethodInvocation):
#         if node.member == 'sort':
#             if node.member in currently_analyzed_methods:
#                 continue  # Skip this occurrence, it's a recursive call
#             else:
#                 currently_analyzed_methods.add(node.member)
#                 count += 1
#     return count