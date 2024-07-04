print("Welcome to your calculator, I am exited to serve you!\n")
print("\nMultiplication = *\nDivision = /\nAddition = +\nSubtraction = -\nTo the power of = **(number)\nRoot = **(1/number)\n")
exit="no"
while exit.lower() in ("no", "no "):
    expr=input("\nInput a valid mathematical expression:  ")
    print()
    try:
        eval(expr)
    except (ValueError, SyntaxError, ZeroDivisionError, TypeError, IndexError) as e:
        print("\n", expr,"  Is not a valid mathematical expression.     ", e, "\n")
        continue
    print("\n", expr, "=", eval(expr))
    exit=input("\n\nDo you want to exit, yes or no: ")