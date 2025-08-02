LENGTH: dict[str, float] = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.344
}

WEIGHT: dict[str, float] = {
    "mg": 0.001,
    "g": 1,
    "kg": 1000,
    "ounces": 28.35,
    "pounds": 453.59
}

def convert_length(value: float, from_unit: str, to_unit: str):
    """Converts length from one unit to another

    Args:
        value (float): Value to be converted
        from_unit (str): Unit to convert from
        to_unit (str): Unit to convert to

    Returns:
        (float): Division of the conversion
    """
    if from_unit == to_unit:
        return value
    
    conversion: float = value * LENGTH[from_unit]
    return round(conversion / LENGTH[to_unit], 2)

def convert_weight(value: float, from_unit: str, to_unit: str):
    """Converts weight from one unit to another

    Args:
        value (float): Value to be converted
        from_unit (str): Unit to convert from
        to_unit (str): Unit to convert to

    Returns:
        (float): Division of the conversion
    """
    if from_unit == to_unit:
        return value
    
    conversion: float = value * WEIGHT[from_unit]
    return round(conversion / WEIGHT[to_unit], 2)
    
def convert_temp(value: float, from_unit: str, to_unit: str):
    """Converts temp from one unit to another

    Args:
        value (float): Value to be converted
        from_unit (str): Unit to convert from
        to_unit (str): Unit to convert to

    Returns:
        (float): Division of the conversion
    """
    value_to_c: float = value

    if from_unit == to_unit:
        return value
    
    if from_unit == "C":
        value_to_c = value
    elif from_unit == "F":
        value_to_c = (value - 32) * 5 / 9
    elif from_unit == "K":
        value_to_c = value - 273.15
    
    if to_unit == "C":
        return value_to_c
    elif to_unit == "F":
        return (value_to_c * 9 / 5) + 32
    elif to_unit == "K":
        return value_to_c + 273.15
