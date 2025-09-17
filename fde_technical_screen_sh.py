def sort(width:int, height:int, length:int, mass:int) -> str:  # Units: cm, kg
    """
    Params:
        width (int): width of package
        height (int): height of package
        length (int): length of package
        mass (int): mass of package
    Returns:
        string: name of stack where package should go
    """
    # CONSTANTS
    BULKY_VOLUME = 1_000_000
    BULKY_DIMENSION = 150
    HEAVY_MASS = 20

    # Validation (Just in case the type hints is not strong enough)
    # Not saving the float conversion just in case imprecision matters
    try:
        float(width)
        float(height)
        float(length)
        float(mass)
    except ValueError as not_float:
        print(f"One or more arguments are not numeric.\nError: {not_float}")

    is_bulky=False
    is_heavy=False
    correct_stack=""

    item_volume = width * height * length
    item_longest_dimension = max(width, height, length)

    if item_volume > BULKY_VOLUME or item_longest_dimension > BULKY_DIMENSION:
        is_bulky = True
    
    if mass > HEAVY_MASS:
        is_heavy = True

    if is_bulky and is_heavy:
        correct_stack="REJECTED"
    elif is_bulky or is_heavy:
        correct_stack="SPECIAL"
    else:
        correct_stack="STANDARD"

    return correct_stack