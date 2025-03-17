import pytest

file_results = {}

def pytest_runtest_logreport(report):
    if report.when == "call":
        file_name = report.nodeid.split("::")[0]
        if file_name not in file_results:
            file_results[file_name] = {"passed": 0, "failed": 0, "total": 0}
        
        if report.passed:
            file_results[file_name]["passed"] += 1
        elif report.failed:
            file_results[file_name]["failed"] += 1
        
        file_results[file_name]["total"] += 1

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    terminalreporter.write_sep("=", "Per-File Test Results")
    for file_name, results in file_results.items():
        passed = results["passed"]
        total = results["total"]
        pass_percentage = (passed / total) * 100 if total > 0 else 0
        terminalreporter.write_line(f"{file_name}: {passed}/{total} passed ({pass_percentage:.2f}%)")