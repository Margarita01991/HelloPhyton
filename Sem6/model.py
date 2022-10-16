import sympy # метод указывает переменную, относительно которй будет решаться уравнение

def evaluate_expr(expr):
    x  = sympy.Symbol('x')
    return sympy.solve(expr,x)