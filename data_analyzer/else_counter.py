import re

import javalang


def count_elses(content):
    tokens = list(javalang.tokenizer.tokenize(content))
    else_count = 0

    for i in range(len(tokens)):
        if tokens[i].value == 'else':
            if tokens[i + 1].value != 'if':
                else_count += 1

    return else_count
