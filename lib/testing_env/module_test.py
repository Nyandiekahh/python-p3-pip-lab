from versions import (
    python_version,
    requests_version,
    pytest_version
)

def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    assert version_info.minor == 12  # Update this to match your current Python minor version

def test_requests_version():
    assert requests_version() == "2.27.1"  # Ensure this matches the version you installed

def test_pytest_version():
    assert pytest_version() == "7.1.3"  # Ensure this matches the version you installed
