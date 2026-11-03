import math

def attendance_percent(attended: int, total: int) -> float:
    if total == 0:
        return 100.0
    return round(attended / total * 100, 2)

def classes_can_skip(attended: int, total: int, min_percent: float = 75) -> int:
    """Max future classes you can miss and stay at or above min_percent."""
    if total == 0:
        return 0
    skip = math.floor(attended * 100 / min_percent - total)
    return max(skip, 0)

def classes_needed(attended: int, total: int, min_percent: float = 75) -> int:
    """Consecutive classes you must attend to reach min_percent."""
    if attendance_percent(attended, total) >= min_percent:
        return 0
    if min_percent >= 100:
        return -1  # impossible once you've missed a class
    need = math.ceil((min_percent * total - 100 * attended) / (100 - min_percent))
    return max(need, 0)