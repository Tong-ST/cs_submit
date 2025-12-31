import check50

@check50.check()
def exists():
    """fuel.py exists"""
    check50.exists("fuel.py")

@check50.check(exists)
def test_e_zero():
    """input of 0/100 yields E"""
    check50.run("python fuel.py").stdin("0/100").stdout("E\n").exit()

@check50.check(exists)
def test_e_one_percent():
    """input of 1/100 yields E"""
    check50.run("python fuel.py").stdin("1/100").stdout("E\n").exit()

@check50.check(exists)
def test_f_full():
    """input of 1/1 yields F"""
    check50.run("python fuel.py").stdin("1/1").stdout("F\n").exit()

@check50.check(exists)
def test_f_ninety_nine():
    """input of 99/100 yields F"""
    check50.run("python fuel.py").stdin("99/100").stdout("F\n").exit()

@check50.check(exists)
def test_fifty_percent():
    """input of 1/2 yields 50%"""
    check50.run("python fuel.py").stdin("1/2").stdout("50%\n").exit()

@check50.check(exists)
def test_twenty_five_percent():
    """input of 1/4 yields 25%"""
    check50.run("python fuel.py").stdin("1/4").stdout("25%\n").exit()

@check50.check(exists)
def test_seventy_five_percent():
    """input of 3/4 yields 75%"""
    check50.run("python fuel.py").stdin("3/4").stdout("75%\n").exit()

@check50.check(exists)
def test_two_percent():
    """input of 2/100 yields 2%"""
    check50.run("python fuel.py").stdin("2/100").stdout("2%\n").exit()

@check50.check(exists)
def test_ninety_eight_percent():
    """input of 98/100 yields 98%"""
    check50.run("python fuel.py").stdin("98/100").stdout("98%\n").exit()

@check50.check(exists)
def test_invalid_input_then_valid():
    """handles non-numeric, division by zero, and x > y inputs"""
    (check50.run("python fuel.py")
            .stdin("cat/dog")
            .stdin("1/0")
            .stdin("5/1")
            .stdin("-1/10")
            .stdin("3/4")
            .stdout("75%\n")
            .exit())