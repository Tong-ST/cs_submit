import check50
import re

@check50.check()
def exists():
    """ตรวจสอบว่ามีไฟล์ fuel.py"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_half():
    """กรอก 1/2 แล้วแสดงผล 50%"""
    check50.run("python3 fuel.py").stdin("1/2", prompt=True).stdout(regex("50%"), "50%", regex=True).exit(0)

@check50.check(exists)
def test_three_quarters():
    """กรอก 3/4 แล้วแสดงผล 75%"""
    check50.run("python3 fuel.py").stdin("3/4", prompt=True).stdout(regex("75%"), "75%", regex=True).exit(0)

@check50.check(exists)
def test_empty():
    """กรอก 0/4 หรือ 1/100 แล้วแสดงผล E"""
    check50.run("python3 fuel.py").stdin("1/100", prompt=True).stdout(regex("E"), "E", regex=True).exit(0)

@check50.check(exists)
def test_full():
    """กรอก 4/4 หรือ 99/100 แล้วแสดงผล F"""
    check50.run("python3 fuel.py").stdin("99/100", prompt=True).stdout(regex("F"), "F", regex=True).exit(0)

@check50.check(exists)
def test_invalid_numerator():
    """กรอก 5/4 (X > Y) โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("5/4", prompt=True).reject()

@check50.check(exists)
def test_zero_division():
    """กรอก 1/0 โปรแกรมจะต้องให้กรอกใหม่ (ZeroDivisionError)"""
    check50.run("python3 fuel.py").stdin("1/0", prompt=True).reject()

@check50.check(exists)
def test_non_integer():
    """กรอก cat/dog โปรแกรมจะต้องให้กรอกใหม่ (ValueError)"""
    check50.run("python3 fuel.py").stdin("cat/dog", prompt=True).reject()

def regex(text):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{re.escape(text)}\s*$'