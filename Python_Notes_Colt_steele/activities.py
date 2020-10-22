def eat(food, is_healthy):
    if not isinstance(is_healthy, bool):
        raise ValueError("is_healthy must be a boolean")
    ending = "because YOLO"
    if is_healthy:
        ending = "because my body is a temple"
    return f"I am eating {food}, {ending}"

def nap(num_hours):
    if num_hours >= 2:
        return f"Uggg!!!. I overslept for {num_hours } hours."
    return "I am feeling refreshed after 1 hour nap"

def is_funny(person):
    if person is "dhinesh": return False
    return True

def laugh():
    return "ha ha ha"