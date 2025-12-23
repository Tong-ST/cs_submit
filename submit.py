import sys
import subprocess
import csv
import json
import re
from datetime import datetime
from pathlib import Path
from tabulate import tabulate


def main():
    arg_len = len(sys.argv)
    if arg_len == 2 and sys.argv[1] == "-sum":
        rows = read_submission()
        lastest = build_overviews(rows)
        show_overview(lastest)
        return

    if arg_len < 3:
        sys.exit("How to submit: python submit.py <assignment_repo> <student_id>")
    problem_path = sys.argv[1]

    cmd = ["check50", "--local", problem_path, "-o", "json"]

    result = subprocess.run(cmd, capture_output=True, text=True)
    assign_name = get_assignment_name(problem_path)[0]
    json_result = result_to_json(result.stdout)
    write_to_json(json_result)

    summary = summarize_result(json_result, 70)
    write_to_csv(json_result, summary, std_id=sys.argv[2], assignment=assign_name)

    print(
        f"{assign_name} — "
        f"{summary['passed_tests']}/{summary['total_tests']} {'✔ passed' if summary['passed'] else '✘ failed'} "
    )


def result_to_json(result):
    try:
        data = json.loads(result)
    except json.JSONDecodeError:
        print("check50 did not return valid JSON")
        print(result)
        exit(1)
    else:
        return data


def write_to_json(json_result):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("data/json_result")
    output_dir.mkdir(parents=True, exist_ok=True)

    json_path = output_dir / f"student_result_{timestamp}.json"

    with open(json_path, "w") as file:
        json.dump(json_result, file, indent=2)


def summarize_result(data, pass_percent):
    results = data.get("results", [])
    total = len(results)
    passed = sum(1 for r in results if r.get("passed"))
    return {
        "total_tests": total,
        "passed_tests": passed,
        "passed": ((passed / total) * 100 >= pass_percent),
    }


def write_to_csv(data, summary, std_id, assignment):
    csv_path = Path("data/submission.csv")
    csv_path.parent.mkdir(parents=True, exist_ok=True)

    row = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "student_id": std_id,
        "assignment": assignment,
        "slug": data.get("slug"),
        "passed": summary["passed"],
        "total_tests": summary["total_tests"],
        "passed_tests": summary["passed_tests"],
    }

    file_exists = csv_path.exists()

    with open(csv_path, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=row.keys())
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)


def get_assignment_name(path):
    pattern = r".+/.+/.+/(.+)"
    matches = re.search(pattern, path, re.IGNORECASE)
    if matches:
        return matches.groups()


def read_submission():
    csv_path = Path("data/submission.csv")
    if not csv_path.exists():
        print("No submission found!")
        return []

    with open(csv_path, newline="") as file:
        reader = csv.DictReader(
            file,
        )
        return list(reader)


def build_overviews(rows):
    overview = {}

    for r in rows:
        key = (r["student_id"], r["assignment"])
        ts = r["timestamp"]

        if key not in overview or ts > overview[key]["timestamp"]:
            overview[key] = r

    return list(overview.values())


def show_overview(rows):
    table = []

    for r in rows:
        status = "PASS" if r["passed"] == "True" else "FAIL"
        table.append(
            [
                r["student_id"],
                r["assignment"],
                status,
                f'{r["passed_tests"]}/{r["total_tests"]}',
                r["timestamp"],
            ]
        )

    headers = ["Student", "Assignment", "Status", "Tests", "Latest Submit"]
    print(tabulate(table, headers=headers, tablefmt="github"))


if __name__ == "__main__":
    main()
