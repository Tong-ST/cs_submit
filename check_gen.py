from google import genai
from dotenv import load_dotenv

load_dotenv()

gemini_model = ["gemini-3-flash-preview", "gemini-2.5-flash", "gemini-3-pro-preview", "gemini-2.5-pro"]


def main():
    assignment_name, assignment_desc, solution_code, pattern, test_amt = create_check_prompt()

    checks = generate_check50_tests(assignment_name, assignment_desc, solution_code, pattern, test_amt)
    print(checks)

    with open("__init__.py", "w") as file:
        file.write(checks)


def call_ai(prompt: str) -> str:
    client = genai.Client()

    response = client.models.generate_content(model=gemini_model[0], contents=prompt)
    return response.text


def build_prompt(name, description, solution, pattern, test_amt=(2, 10)):
    return f'''
    You are an assistant helping instructors write check50 tests.

    Assignment name: {name}

    Assignment description:
    {description}

    Reference solution (correct behavior):
    {solution}

    Reference good check pattern:
    {pattern}
    
    Requirements:
    - Use check50 Python API
    - Include a file existence check
    - Test valid input
    - Test invalid input and re-prompt
    - Do NOT include explanations, only code
    - Do NOT include ``` python ``` just ready to use code
    - Use check50.run(), stdin(), stdout()
    - For try & except test, Can use .reject() to pass the test
    - Test explaination in Thai For Example กรอก input ... ได้ Output คือ ...
    - Minimum test function is {test_amt[0]} and Maximum is {test_amt[1]}
    - ONLY ONE check50.run() for each check function created

    Output ONLY valid Python code.
    '''

def generate_check50_tests(assignment_name, assignment_description, reference_solution, pattern, test_amt):
    prompt = build_prompt(assignment_name, assignment_description, reference_solution, pattern, test_amt)

    code = call_ai(prompt)

    return code


def create_check_prompt():
    assignment_name = "fuel"
    assignment_desc = '''
    Write a program fuel.py that:
    - Prompts for X/Y
    - Re-prompts until valid
    - Prints E, F, or percentage
    - Replicate of car fuel gauge
    '''

    solution_code = '''
    while True:
        try:
            fuel = input("Fraction: ")
            x, y = fuel.split("/")
            if int(x) > int(y) or int(x) < 0:
                raise ValueError
            percent = round((int(x) / int(y)) * 100)
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break

    if percent >= 99:
        print("F")
    elif percent <= 1:
        print("E")
    else:
        print(f"{percent}%")
    '''

    pattern = '''
    import check50 # A MUST
    import re # OPTIONAL FOR regex test

    @check50.check() # A MUST to create each check
    def exists(): # A MUST for most assignment
        """ตรวจสอบว่ามีไฟล์ file.py""" # Test explaination
        check50.exists("file.py") # Check if required file exists?

    @check50.check(exists) # Need to pass file exists check function before can run this test
    def test_valid_function():
        """กรอก input ... ได้ผลลัพธ์ ..."""
        input = "..."
        output = "..."
        check50.run("python3 file.py").stdin(input, prompt=True).stdout(regex(output), output, regex=True).exit() # Test logic

        # ONLY ONE check50.run() for each check function created

    @check50.check(exists)
    def test_invalid_function(): # ONLY IF assignment require try & except logic
        """กรอก input ... โปรแกรมจะต้องให้กรอกใหม่ """
        input = "..."
        check50.run("python3 file.py").stdin(input, prompt=True).reject() # Test try & except use .reject() for invalid to pass the test

        # ONLY ONE check50.run() for each check function created

    def regex(text): # OPTIONAL helper function for ouput correctness
        """match case-insensitively with only whitespace on either side"""
        return fr'(?i)^*{re.escape(text)}*$'
    '''
    
    test_amt = (4, 8)

    return assignment_name, assignment_desc, solution_code, pattern, test_amt


if __name__ == "__main__":
    main()
