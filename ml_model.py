def predict_value(value):
    """
    Simple ML simulation:
    If value > 50 => "High"
    else => "Low"
    """
    try:
        value = float(value)
    except:
        return "Invalid"

    return "High" if value > 50 else "Low"