import javalang
from javalang.ast import Node
from javalang.tree import (AssertStatement, BlockStatement, BreakStatement,
                           ContinueStatement, DoStatement, ForStatement,
                           IfStatement, ReturnStatement, SwitchStatement,
                           SynchronizedStatement, ThrowStatement, TryStatement,
                           WhileStatement)


def count_statements(content):
    state_counter = 0
    tree = javalang.parse.parse(content)
    state_counter += sum(1 for _, node in tree.filter(AssertStatement))
    state_counter += sum(1 for _, node in tree.filter(BlockStatement))
    state_counter += sum(1 for _, node in tree.filter(BreakStatement))
    state_counter += sum(1 for _, node in tree.filter(ContinueStatement))
    state_counter += sum(1 for _, node in tree.filter(DoStatement))
    state_counter += sum(1 for _, node in tree.filter(ForStatement))
    state_counter += sum(1 for _, node in tree.filter(IfStatement))
    state_counter += sum(1 for _, node in tree.filter(ReturnStatement))
    state_counter += sum(1 for _, node in tree.filter(SwitchStatement))
    state_counter += sum(1 for _, node in tree.filter(SynchronizedStatement))
    state_counter += sum(1 for _, node in tree.filter(ThrowStatement))
    state_counter += sum(1 for _, node in tree.filter(TryStatement))
    state_counter += sum(1 for _, node in tree.filter(WhileStatement))
    return state_counter 

    