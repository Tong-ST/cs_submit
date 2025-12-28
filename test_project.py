from project import summarize_result, result_to_json, get_assignment_name
import pytest

def test_summarize_result_pass():
    data = {
        "results": [
            {"passed": True},
            {"passed": True},
            {"passed": False},
        ]
    }

    summary = summarize_result(data, pass_percent=60)

    assert summary["total_tests"] == 3
    assert summary["passed_tests"] == 2
    assert summary["passed"] is True


def test_summarize_result_fail():
    data = {
        "results": [
            {"passed": True},
            {"passed": False},
        ]
    }

    summary = summarize_result(data, pass_percent=75)

    assert summary["passed"] is False


def test_result_to_json_valid():
    raw = '{"results": [{"passed": true}]}'
    data = result_to_json(raw)
    assert data["results"][0]["passed"] is True


def test_result_to_json_invalid():
    with pytest.raises(ValueError):
        result_to_json("definately not json")



def test_get_assignment_name_returns_string():
    path = "Tong-ST/problems/main/ps_test"
    result = get_assignment_name(path)
    assert result == "ps_test"

def test_get_assignment_name_returns_none_for_short_path():
    assert get_assignment_name("ps_test") is None

def test_get_assignment_name_mixed_case():
    path = "TONG-ST/Problems/Main/PS_Test"
    assert get_assignment_name(path) == "PS_Test"
