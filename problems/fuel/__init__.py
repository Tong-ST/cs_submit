import check50

@check50.check()
def exists():
    """ตรวจสอบว่ามีไฟล์ fuel.py อยู่หรือไม่"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_valid_half():
    """เมื่อกรอก input "1/2" โปรแกรมควรแสดงผลเป็น "50%" """
    check50.run("python3 fuel.py").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_valid_quarter():
    """เมื่อกรอก input "1/4" โปรแกรมควรแสดงผลเป็น "25%" """
    check50.run("python3 fuel.py").stdin("1/4").stdout("25%\n").exit(0)

@check50.check(exists)
def test_valid_exact_zero():
    """เมื่อกรอก input "0/1" โปรแกรมควรแสดงผลเป็น "E" """
    check50.run("python3 fuel.py").stdin("0/1").stdout("E\n").exit(0)

@check50.check(exists)
def test_valid_one_percent():
    """เมื่อกรอก input "1/100" โปรแกรมควรแสดงผลเป็น "E" """
    check50.run("python3 fuel.py").stdin("1/100").stdout("E\n").exit(0)

@check50.check(exists)
def test_valid_ninety_nine_percent():
    """เมื่อกรอก input "99/100" โปรแกรมควรแสดงผลเป็น "F" """
    check50.run("python3 fuel.py").stdin("99/100").stdout("F\n").exit(0)

@check50.check(exists)
def test_valid_full():
    """เมื่อกรอก input "1/1" โปรแกรมควรแสดงผลเป็น "F" """
    check50.run("python3 fuel.py").stdin("1/1").stdout("F\n").exit(0)

@check50.check(exists)
def test_valid_round_up_mid_point():
    """เมื่อกรอก input "1/200" (0.5% -> 1%) โปรแกรมควรแสดงผลเป็น "E" """
    check50.run("python3 fuel.py").stdin("1/200").stdout("E\n").exit(0)

@check50.check(exists)
def test_valid_round_down_below_mid_point():
    """เมื่อกรอก input "1/201" (0.49% -> 0%) โปรแกรมควรแสดงผลเป็น "E" """
    check50.run("python3 fuel.py").stdin("1/201").stdout("E\n").exit(0)

@check50.check(exists)
def test_valid_round_up_to_f_mid_point():
    """เมื่อกรอก input "199/200" (99.5% -> 100%) โปรแกรมควรแสดงผลเป็น "F" """
    check50.run("python3 fuel.py").stdin("199/200").stdout("F\n").exit(0)

@check50.check(exists)
def test_valid_round_down_to_99():
    """เมื่อกรอก input "9949/10000" (99.49% -> 99%) โปรแกรมควรแสดงผลเป็น "F" """
    check50.run("python3 fuel.py").stdin("9949/10000").stdout("F\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_zero_division():
    """เมื่อกรอก input ที่ Y เป็นศูนย์ ("1/0") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("1/0").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_value_error_x_greater_y():
    """เมื่อกรอก input ที่ X มากกว่า Y ("2/1") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("2/1").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_value_error_x_negative():
    """เมื่อกรอก input ที่ X เป็นค่าติดลบ ("-1/2") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("-1/2").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_not_integer():
    """เมื่อกรอก input ที่ไม่ใช่ตัวเลข ("cat/dog") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("cat/dog").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_no_slash():
    """เมื่อกรอก input ที่ไม่มีเครื่องหมายทับ ("1 2") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("1 2").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_too_many_slashes():
    """เมื่อกรอก input ที่มีเครื่องหมายทับมากเกินไป ("1/2/3") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("1/2/3").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_empty_input():
    """เมื่อกรอก input ที่ว่างเปล่า ("") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_non_numeric_x():
    """เมื่อกรอก input ที่ X ไม่ใช่ตัวเลข ("a/2") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("a/2").stdin("1/2").stdout("50%\n").exit(0)

@check50.check(exists)
def test_invalid_then_valid_non_numeric_y():
    """เมื่อกรอก input ที่ Y ไม่ใช่ตัวเลข ("1/b") แล้วตามด้วย input ที่ถูกต้อง ("1/2") โปรแกรมควรร้องขอ input ใหม่แล้วแสดงผลที่ถูกต้อง"""
    check50.run("python3 fuel.py").stdin("1/b").stdin("1/2").stdout("50%\n").exit(0)