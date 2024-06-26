import pytest
from pathlib import Path


#
# @pytest.fixture(scope="session")
# def browser_context_args(browser_context_args):
#     return {
#         **browser_context_args,
#         "record_video_dir": "test-reports/videos/"
#     }


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    report = outcome.get_result()

    # Set an attribute for each phase of a call, which can be "setup", "call", "teardown"
    setattr(item, "rep_" + report.when, report)


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args, request):
    return {
        **browser_context_args,
        "record_video_dir": Path("test-results/videos").resolve() if request.node.rep_call.failed else None
    }