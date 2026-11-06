
def parse(expr):
    expr = expr.replace(" ", "")
    name, args = expr.split("(", 1)
    args = args.rstrip(")").split(",")
    return (name, *args)


def is_variable(x):
    return isinstance(x, str) and len(x) == 1 and x.islower()


def substitute(x, subs):
    while isinstance(x, str) and x in subs:
        x = subs[x]

    if isinstance(x, tuple):
        return tuple(substitute(i, subs) for i in x)

    return x


def occurs_check(var, expr, subs):
    expr = substitute(expr, subs)

    if var == expr:
        return True

    if isinstance(expr, tuple):
        return any(occurs_check(var, i, subs) for i in expr)

    return False


def unify(x, y, subs):
    x = substitute(x, subs)
    y = substitute(y, subs)

    if x == y:
        return True

    if is_variable(x):
        if occurs_check(x, y, subs):
            return False
        subs[x] = y
        return True

    if is_variable(y):
        if occurs_check(y, x, subs):
            return False
        subs[y] = x
        return True

    if isinstance(x, tuple) and isinstance(y, tuple):

        if len(x) != len(y) or x[0] != y[0]:
            return False

        for a, b in zip(x[1:], y[1:]):
            if not unify(a, b, subs):
                return False

        return True

    return False


# Main Program
print("FIRST ORDER LOGIC - UNIFICATION")

expr1 = input("Enter first expression: ")
expr2 = input("Enter second expression: ")

x = parse(expr1)
y = parse(expr2)

subs = {}

if unify(x, y, subs):
    print("\nUnification Successful!")

    print("Substitution:", subs)

    unified = substitute(x, subs)

    # Convert tuple into predicate notation
    unified_expression = unified[0] + "(" + ", ".join(unified[1:]) + ")"

    print("Unified Expression:", unified_expression)

else:
    print("\nUnification Failed!")


print ("Ashmitha Sasikumar - 1WA24CS065")