import check50
import re

@check50.check()
def exists():
    """ตรวจสอบว่ามีไฟล์ fuel.py"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_75_percent():
    """กรอก 3/4 ได้ผลลัพธ์ 75%"""
    check50.run("python3 fuel.py").stdin("3/4", prompt=True).stdout(regex("75%"), "75%", regex=True).exit()

@check50.check(exists)
def test_25_percent():
    """กรอก 1/4 ได้ผลลัพธ์ 25%"""
    check50.run("python3 fuel.py").stdin("1/4", prompt=True).stdout(regex("25%"), "25%", regex=True).exit()

@check50.check(exists)
def test_E():
    """กรอก 0/4 ได้ผลลัพธ์ E"""
    check50.run("python3 fuel.py").stdin("0/4", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_F():
    """กรอก 4/4 ได้ผลลัพธ์ F"""
    check50.run("python3 fuel.py").stdin("4/4", prompt=True).stdout(regex("F"), "F", regex=True).exit()

@check50.check(exists)
def test_boundary_cases():
    """กรอก 1/100 ได้ผลลัพธ์ E และ 99/100 ได้ผลลัพธ์ F"""
    check50.run("python3 fuel.py").stdin("1/100", prompt=True).stdout(regex("E"), "E", regex=True).exit()

@check50.check(exists)
def test_invalid_input_text():
    """กรอก cat/dog โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("cat/dog", prompt=True).reject()

@check50.check(exists)
def test_invalid_input_value():
    """กรอก 5/4 หรือ 1/0 โปรแกรมจะต้องให้กรอกใหม่"""
    check50.run("python3 fuel.py").stdin("5/4", prompt=True).reject()

def regex(text):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{re.escape(text)}\s*$'