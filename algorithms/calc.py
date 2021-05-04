
def calc(expression):
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = "ERROR"
    return result

