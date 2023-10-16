import ast
import re

import javalang


def count_minMax(content):
    # Parse the Java code
    tree = javalang.parse.parse(content)

    # Initialize counters
    min_calls = 0
    max_calls = 0

    # Traverse the syntax tree to count calls to min() and max()
    for path, node in tree:
        if isinstance(node, javalang.tree.MethodInvocation):
            method_name = node.member
            if method_name == "min":
                min_calls += 1
            elif method_name == "max":
                max_calls += 1

    return min_calls + max_calls

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