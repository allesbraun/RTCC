import javalang


#LocalVariableDeclaration + VariableDeclaration
def count_variables(content):
    tree = javalang.parse.parse(content)
    count = 0

    # count += sum(1 for _ in tree.filter(javalang.tree.LocalVariableDeclaration))
    count += sum(1 for _ in tree.filter(javalang.tree.VariableDeclaration))

    return count 
