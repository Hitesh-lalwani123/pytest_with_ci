# tests/unit/test_module1.py
import pytest

@pytest.mark.unit
def test_add():
    assert 1 + 1 == 2

# tests/integration/test_integration.py
@pytest.mark.integration
def test_integration():
    assert 2 * 2 == 4

# tests/functional/test_functional.py
@pytest.mark.functional
def test_functional():
    assert "hello".upper() == "HELLO"