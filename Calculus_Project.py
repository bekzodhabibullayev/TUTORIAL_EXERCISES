RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"
def show_all_functions():
    print(f"\n{BOLD}AVAILABLE FUNCTIONS YOU MAY ENTER{RESET}\n")

    # Exponential
    print(f"{BOLD}EXPONENTIAL{RESET}")
    print("  e^x        a^x   (example: 2^x)")
    print()

    # Logarithmic
    print(f"{BOLD}LOGARITHMIC{RESET}")
    print("  lnx        logx  (base 10)")
    print()

    # Trigonometric (bold title; functions plain)
    print(f"{BOLD}TRIGONOMETRIC{RESET}")
    print("  sinx   cosx   tanx  (or tgx)   cotx  (or ctgx)")
    print("  secx   cscx")
    print()

    # Inverse trig
    print(f"{BOLD}INVERSE TRIGONOMETRIC{RESET}")
    print("  arcsinx   arccosx   arctanx   arccotx")
    print()

    # Hyperbolic
    print(f"{BOLD}HYPERBOLIC{RESET}")
    print("  sinhx   coshx   tanhx   cothx   sechx   cschx")
    print()

    # Inverse hyperbolic
    print(f"{BOLD}INVERSE HYPERBOLIC{RESET}")
    print("  arsinhx  arcoshx  artanhx  arcothx  arsechx  arcschx")
    print()

    # Polynomials & algebraic
    print(f"{BOLD}POLYNOMIAL / POWER / SIMPLE FORMS{RESET}")
    print("  x   x^2   x^n   3x^2   -2x^3   (use x^n or x**n)")
    print()

    print("Type 'list' to show this menu again, 'quit' to exit.\n")
def separator():
    print(f"{RED}{'●'*36}{RESET}\n")

def derivative_of(expr):
    e = expr.lower().replace(" ", "")

    if e == "sinx": return "cosx"
    if e == "cosx": return "-sinx"
    if e in ("tanx", "tgx"): return "sec^2x  (or 1/cos^2x)"
    if e in ("cotx", "ctgx"): return "-csc^2x  (or -1/sin^2x)"
    if e == "secx": return "secx * tanx"
    if e == "cscx": return "-cscx * cotx"

    if e in ("arcsinx", "asinx"): return "1 / sqrt(1 - x^2)"
    if e in ("arccosx", "acosx"): return "-1 / sqrt(1 - x^2)"
    if e in ("arctanx", "atanx"): return "1 / (1 + x^2)"
    if e in ("arccotx", "acotx"): return "-1 / (1 + x^2)"

    if e in ("e^x", "ex", "exp(x)"): return "e^x"
    if "^x" in e and not e.startswith("x^"):
        base = e.split("^",1)[0]
        if base == "e": return "e^x"
        return f"{base}^x * ln({base})"

    if e in ("lnx", "ln(x)"): return "1 / x"
    if e in ("logx", "log(x)"): return "1 / (x * ln(10))"

    if e == "x": return "1"
    if e in ("x^2", "x**2"): return "2x"
    if e in ("x^3", "x**3"): return "3x^2"
    if e.startswith("x^") or e.startswith("x**"):
        if "^" in e:
            power = e.split("^",1)[1]
        else:
            power = e.split("**",1)[1]
        try:
            n = int(float(power))
            return f"{n}x^{n-1}  (power rule)"
        except:
            return f"n*x^(n-1)  (you entered x^{power})"

    s = e.replace("**","^")
    if "x^" in s and s.count("^") == 1 and "x" in s:
        idx = s.find("x")
        coef = s[:idx]
        power = s.split("^",1)[1]
        if coef == "" or coef == "+": coef_val = "1"
        elif coef == "-": coef_val = "-1"
        else: coef_val = coef
        try:
            n = int(float(power))
            return f"{coef_val}*{n}*x^{n-1}  (i.e., {coef_val}{n}x^{n-1})"
        except:
            return f"{coef_val}*n*x^(n-1)  (power rule)"

    if e in ("sinhx","sinh(x)"):
        return ("coshx  (similar to sinx → cosx)\n"
                "💡 sinhx = (e^x - e^(-x)) / 2")
    if e in ("coshx","cosh(x)"):
        return ("sinhx  (similar to cosx → -sinx but without minus)\n"
                "💡 coshx = (e^x + e^(-x)) / 2")
    if e in ("tanhx","tanh(x)"):
        return "1 - tanh^2x  (also written sech^2x)  (tanh ~ tan)"
    if e in ("cothx","coth(x)"):
        return "1 - coth^2x  (hyperbolic cotan form)"
    if e in ("sechx","sech(x)"):
        return "-sechx * tanhx"
    if e in ("cschx","csch(x)"):
        return "-cschx * cothx"

    if e in ("arsinhx","asinhx"): return "1 / sqrt(1 + x^2)"
    if e in ("arcoshx","acoshx"): return "1 / sqrt(x^2 - 1)"
    if e in ("artanhx","atanhx"): return "1 / (1 - x^2)"

    return None  

print(f"{BOLD}DERIVATIVE TRAINER{RESET}")
show_all_functions()
separator()

while True:
    user = input("Enter a function (or 'list' to show functions, 'quit' to exit): ").strip()
    if user.lower() == "quit":
        print("\nGood work — keep practicing! 👋")
        break
    if user.lower() == "list":
        show_all_functions()
        separator()
        continue

    ans = derivative_of(user)
    print() 
    if ans is None:
        print("Sorry — I don't recognize that exact pattern. Try something from the list.")
    else:
        print(f"Derivative of {user}  →  {ans}")

    separator()