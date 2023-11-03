import javalang


def count_ifs(content):
    tokens = javalang.tokenizer.tokenize(content)
    count = 0
    for token in tokens:
        if isinstance(token, javalang.tokenizer.Keyword) and token.value == 'if':
            count += 1
    return count
