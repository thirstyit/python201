# Add a Google-style docstring to the function below. Your docstring
# should at least describe what it does, what arguments it takes,
# and what it returns.

def km_to_miles(km):
    """Converts kilometers to miles.

    Args:
        km (float): An amount of kilometers, can also be int

    Returns:
        float: The converted amount in miles
    """
    miles = km * 0.6
    return miles

print(km_to_miles.__doc__)
