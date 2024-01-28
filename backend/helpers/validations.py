from datetime import datetime

def validate_integer(value, field_name):
    if value is not None:
        try:
            value = int(float(value))
            if value < 0:
                raise ValueError(f"{field_name} must be a valid non-negative integer or a float.")
        except (ValueError, TypeError):
            raise TypeError(f"{field_name} must be a valid non-negative integer or a float.")
    else:
        raise ValueError(f"{field_name} cannot be None.")
    
    return value

def validate_time(time):
    if time is None:
        raise ValueError("'time' cannot be None.")
    elif time == "":
        raise ValueError("'time' cannot be an empty string.")
    elif isinstance(time, datetime):
        return str(time)
    elif not isinstance(time, str):
        raise ValueError("Invalid 'time' format. It should be a valid date, a datetime object, or a string.")
    else:
        try:
            parsed_time = datetime.fromisoformat(time)
            return str(parsed_time)
        except ValueError:
            raise ValueError("Invalid 'time' format. It should be a valid date, a datetime object, or a string.")