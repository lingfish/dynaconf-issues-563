import pytest
from config import settings

@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    """Forces usage of [testing] env from `settings.toml` for tests"""
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
  
def test_running_on_testing_environment():
    assert settings.current_env == "testing"
    assert settings.ENV_FOR_DYNACONF == "testing"
    
