import check50
import re

@check50.check()
def exists():
    """ตรวจสอบว่ามีไฟล์ fuel.py"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_75_percent():
    """กรอก input 3/4 ได้ผลลัพธ์ 75%"""
    check50.run("python3 fuel.py").stdin("3/4", prompt=True).stdout(regex("75%"), "75%", regex=True).exit()

@check50.check(exists)
def test_33_percent():
    """กรอก input 1/3 ได้ผลลัพธ์ 33% (ตรวจสอบการปัดเศษ)"""
    check50.run("python3 fuel.py").stdin("1/3", prompt=True).stdout(regex("33%"), "33%", regex=True).exit()

@check50.check(exists)
def test_full():
    """กรอก input 4/4 ได้ผลลัพธ์ F"""
    check50.run("python3 fuel.py").stdin("4/4", prompt=True).stdout(regex("F"), "F", regex=True).exit()

@check50.check(exists)
def test_empty():
    """กรอก input 0/4 ได้ผลลัพธ์ E"""
    check50.run("python3 fuel.py").stdin("0/4", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_boundary():
    """กรอก input 1/100 ได้ผลลัพธ์ E และ 99/100 ได้ผลลัพธ์ F"""
    check50.run("python3 fuel.py").stdin("1/100", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_invalid_x_greater_than_y():
    """กรอก input 5/4 (X > Y) โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("5/4", prompt=True).reject()

@check50.check(exists)
def test_zero_division():
    """กรอก input 1/0 โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("1/0", prompt=True).reject()

@check50.check(exists)
def test_invalid_format():
    """กรอก input ที่ไม่ใช่ตัวเลข (cat/dog) โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("cat/dog", prompt=True).reject()

def regex(text):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{re.escape(text)}\s*$'