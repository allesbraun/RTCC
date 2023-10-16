import javalang


def count_breaks(content):
    tokens = javalang.tokenizer.tokenize(content)
    count = 0
    for token in tokens:
        if isinstance(token, javalang.tokenizer.Keyword) and token.value == 'break':
            count += 1
    return count