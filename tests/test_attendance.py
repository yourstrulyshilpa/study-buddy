from core.attendance import attendance_percent, classes_can_skip, classes_needed

def test_percent():
    assert attendance_percent(30, 40) == 75.0

def test_can_skip():
    assert classes_can_skip(30, 36, 75) == 4   # 30/40 = 75%

def test_needed():
    assert classes_needed(20, 30, 75) == 10    # 30/40 = 75%