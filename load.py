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


def minimize_test_suite(testcase_coverage, requirements):
    uncovered = set(requirements)
    selected_tests = []

    while uncovered:
        best_tc = None
        best_cover = set()
        for tc, covers in testcase_coverage.items():
            covered = set(covers) & uncovered
            if len(covered) > len(best_cover):
                best_tc = tc
                best_cover = covered

        if not best_tc:
            break

        selected_tests.append(best_tc)
        uncovered -= best_cover

    return selected_tests

