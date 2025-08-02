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
    
