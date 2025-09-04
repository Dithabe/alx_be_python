#typeError - built in
#ZeroDivision Error - also built in
def safe_divide(numerator, denominator):

    try:
        num = float(numerator)
        deno = float(denominator)
        if deno == 0:
            raise ZeroDivisionError("Error: Cannot divide by zero.")
        return float(num / deno)

    except ValueError:
        return "Error: Please enter numeric values only." 
        