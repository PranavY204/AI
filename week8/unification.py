class UnificationError(Exception):
    pass

def unify(expr1, expr2, substitutions=dict()):
    # if substitutions is None:
    #     substitutions = {}

    # If both expressions are identical, return current substitutions
    if expr1 == expr2:
        return substitutions

    # If the first expression is a variable
    if is_variable(expr1):
        return unify_variable(expr1, expr2, substitutions)

    # If the second expression is a variable
    if is_variable(expr2):
        return unify_variable(expr2, expr1, substitutions)

    # If both expressions are compound expressions
    if is_compound(expr1) and is_compound(expr2):
        if expr1[0] != expr2[0] or len(expr1[1:]) != len(expr2[1:]):
            raise UnificationError("Expressions do not match.")
        return unify_lists(expr1[1:], expr2[1:], unify(expr1[0], expr2[0], substitutions))

    # If expressions are not compatible
    raise UnificationError(f"Cannot unify {expr1} and {expr2}.")

def unify_variable(var, expr, substitutions):
    if var in substitutions:
        return unify(substitutions[var], expr, substitutions)
    elif occurs_check(var, expr, substitutions):
        raise UnificationError(f"Occurs check failed: {var} in {expr}.")
    else:
        substitutions[var] = expr
        return substitutions

def unify_lists(list1, list2, substitutions):
    for expr1, expr2 in zip(list1, list2):
        substitutions = unify(expr1, expr2, substitutions)
    return substitutions

def is_variable(term):
    return isinstance(term, str) and term[0].islower()

def is_compound(term):
    return isinstance(term, (list, tuple)) and len(term) > 0

def occurs_check(var, expr, substitutions):
    if var == expr:
        return True
    elif is_compound(expr):
        return any(occurs_check(var, sub, substitutions) for sub in expr)
    elif expr in substitutions:
        return occurs_check(var, substitutions[expr], substitutions)
    return False
