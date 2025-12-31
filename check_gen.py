from google import genai
from dotenv import load_dotenv

load_dotenv()


def main():
    assignment_name, assignment_desc, solution_code = create_check_prompt()

    checks = generate_check50_tests(assignment_name, assignment_desc, solution_code)

    with open("__init__.py", "w") as file:
        file.write(checks)


def call_ai(prompt: str) -> str:
    client = genai.Client()

    response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
    return response.text


def build_prompt(name, description, solution):
    return f"""
    You are an assistant helping instructors write check50 tests.

    Assignment name: {name}

    Assignment description:
    {description}

    Reference solution (correct behavior):
    {solution}

    Requirements:
    - Use check50 Python API
    - Include a file existence check
    - Test valid input
    - Test invalid input and re-prompt
    - Do NOT include explanations, only code
    - Use check50.run(), stdin(), stdout()
    - just pure code ready to use __init__.py file

    Output ONLY valid Python code.
    """


def generate_check50_tests(assignment_name, assignment_description, reference_solution):
    prompt = build_prompt(assignment_name, assignment_description, reference_solution)

    code = call_ai(prompt)

    return code


def create_check_prompt():
    assignment_name = "fuel"
    assignment_desc = """
    Write a program fuel.py that:
    - Prompts for X/Y
    - Re-prompts until valid
    - Prints E, F, or percentage
    """

    solution_code = """
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
    """
    return assignment_name, assignment_desc, solution_code


if __name__ == "__main__":
    main()
