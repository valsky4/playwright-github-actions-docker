import pytest
from pathlib import Path


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_dir": "test-reports/videos/"
    }
