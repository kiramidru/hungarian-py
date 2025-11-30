import json
import importlib


def load_requirements_names():
    with open("requirement.json") as f:
        data = json.load(f)
    return list(data.keys())


def load_requirements():
    requirements = []

    with open("requirement.json") as f:
        data = json.load(f)

    func_module = importlib.import_module("functions")
    requirements = []

    for _, func_name in data.items():
        func = getattr(func_module, func_name)
        requirements.append(func)

    return requirements


def load_test_cases():
    testcases = []

    with open("testcase.json") as f:
        data = json.load(f)
        testcases = list(data.values())
    return testcases


def load_testcase_coverage():
    testcase_coverage = []

    with open("testcase_coverage.json") as f:
        testcase_coverage = json.load(f)
    return testcase_coverage
