# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """

    This converter converts km to miles.

    input km -> num
    returns ,miles -> num

    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
