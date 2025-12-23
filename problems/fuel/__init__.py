import check50
from re import escape


@check50.check()
def exists():
    """fuel.py exists"""
    check50.exists("fuel.py")


@check50.check(exists)
def test_3_over_4():
    """กรอก input 3/4 ต้องได้ output คือ 75%"""
    input = "3/4"
    output = "75%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_round_down():
    """กรอก input 1/3 ต้องได้ output คือ 33%"""
    input = "1/3"
    output = "33%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_round_up():
    """กรอก input 2/3 ต้องได้ output คือ 67%"""
    input = "2/3"
    output = "67%"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_empty():
    """กรอก input 0/100 ต้องได้ output คือ E"""
    input = "0/100"
    output = "E"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()


@check50.check(exists)
def test_full():
    """กรอก input 100/100 ต้องได้ output คือ F"""
    input = "100/100"
    output = "F"
    check50.run("python3 fuel.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit()



@check50.check(exists)
def test_ZeroDivisionError():
    """กรอก input 100/0 โปรแกรมต้องให้กรอก input ใหม่"""
    input = "100/0"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_numerator_greater_than_denominator():
    """กรอก input 10/3 โปรแกรมต้องให้กรอก input ใหม่"""
    input = "10/3"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_str_conversion():
    """กรอก input three/four โปรแกรมต้องให้กรอก input ใหม่"""
    input = "three/four"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_float_numerator(): 
    """กรอก input 1.5/4 โปรแกรมต้องให้กรอก input ใหม่"""
    input = "1.5/4"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


@check50.check(exists)
def test_negative_fraction():
    """กรอก input -1/4 โปรแกรมต้องให้กรอก input ใหม่"""
    input = "-1/4"
    check50.run("python3 fuel.py").stdin(input, prompt=True).reject()


def regex(percent):
    """match case-insensitively with only whitespace on either side"""
    return fr'(?i)^\s*{escape(percent)}\s*$'