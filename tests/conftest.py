import tempfile
from pathlib import Path

import pytest


@pytest.fixture
def temp_directory():
    """Create a temporary working directory."""
    with tempfile.TemporaryDirectory() as directory:
        yield Path(directory)


@pytest.fixture
def sample_question():
    return "What should be inspected when hydraulic pressure drops during landing gear extension?"


@pytest.fixture
def sample_failure():
    return (
        "Hydraulic system pressure drops during landing gear extension."
    )