def grade_to_points(grade: str, university: str = "default") -> float:
    return 8.0  # STUB

def calculate_sgpa(courses: list[dict]) -> float:
    """courses = [{"credits": 4, "grade": "A"}, ...]"""
    return 7.5  # STUB

def calculate_cgpa(semesters: list[list[dict]]) -> float:
    return 7.5  # STUB

def required_sgpa(current_cgpa: float, credits_done: float,
                  next_credits: float, target: float) -> float:
    return 8.0  # STUB