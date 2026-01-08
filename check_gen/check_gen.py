from google import genai
from dotenv import load_dotenv
import yaml

load_dotenv()

gemini_model = [
    "gemini-3-flash-preview",
    "gemini-2.5-flash",
    "gemini-3-pro-preview",
    "gemini-2.5-pro",
]


def main():
    assignment = load_yaml("assignments/fuel.yaml")
    patterns = load_yaml("patterns.yaml")

    checks = generate_check50_tests(assignment, patterns["INOUT_CHECK"])
    print(checks)

    with open("__init__.py", "w") as file:
        file.write(checks)


def load_yaml(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def call_ai(prompt: str) -> str:
    client = genai.Client()

    response = client.models.generate_content(model=gemini_model[0], contents=prompt)
    return response.text


def build_prompt(assignment, pattern):
    return f"""
    You are an assistant helping instructors write check50 tests.

    Assignment name: {assignment["assignment_name"]}

    Assignment description:
    {assignment["assignment_desc"]}

    Reference solution (correct behavior):
    {assignment["solution_code"]}

    Reference good check pattern:
    {pattern}
    
    Requirements:
    - Use check50 API
    - Only code output
    - One run per test
    - Do NOT include ``` python ```, ONLY READY TO USE CODE
    - Thai descriptions
    - Minimum tests function is {assignment['test_amount']['min']} and Maximum is: {assignment['test_amount']['max']}
    """


def generate_check50_tests(
    assignment,
    pattern,
):
    prompt = build_prompt(assignment, pattern)

    code = call_ai(prompt)

    return code


if __name__ == "__main__":
    main()
