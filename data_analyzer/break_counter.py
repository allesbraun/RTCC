import javalang


def count_breaks(content):
    try:
        tokens = javalang.tokenizer.tokenize(content)
        count = 0
        for token in tokens:
            if isinstance(token, javalang.tokenizer.Keyword) and token.value == 'break':
                count += 1
        return count
    except javalang.parser.JavaSyntaxError as e:
        print(f"Erro de sintaxe Java: {e}")