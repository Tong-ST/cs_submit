import check50
import re

@check50.check()
def exists():
    """ตรวจสอบว่ามีไฟล์ fuel.py"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_75_percent():
    """กรอก 3/4 และตรวจสอบว่าแสดงผล 75%"""
    check50.run("python3 fuel.py").stdin("3/4", prompt=True).stdout(regex("75%"), "75%", regex=True).exit()

@check50.check(exists)
def test_full():
    """กรอก 4/4 และตรวจสอบว่าแสดงผล F"""
    check50.run("python3 fuel.py").stdin("4/4", prompt=True).stdout(regex("F"), "F", regex=True).exit()

@check50.check(exists)
def test_empty():
    """กรอก 0/4 และตรวจสอบว่าแสดงผล E"""
    check50.run("python3 fuel.py").stdin("0/4", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_99_percent():
    """กรอก 99/100 และตรวจสอบว่าแสดงผล F (มากกว่าหรือเท่ากับ 99%)"""
    check50.run("python3 fuel.py").stdin("99/100", prompt=True).stdout(regex("F"), "F", regex=True).exit()

@check50.check(exists)
def test_1_percent():
    """กรอก 1/100 และตรวจสอบว่าแสดงผล E (น้อยกว่าหรือเท่ากับ 1%)"""
    check50.run("python3 fuel.py").stdin("1/100", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_invalid_x_greater_than_y():
    """กรอก 5/4 (X > Y) และโปรแกรมต้องขอ input ใหม่"""
    check50.run("python3 fuel.py").stdin("5/4", prompt=True).reject()

@check50.check(exists)
def test_invalid_input_type():
    """กรอก cat/dog หรือ 1/0 และโปรแกรมต้องขอ input ใหม่"""
    check50.run("python3 fuel.py").stdin("cat/dog", prompt=True).reject()

def regex(text):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{re.escape(text)}\s*$'