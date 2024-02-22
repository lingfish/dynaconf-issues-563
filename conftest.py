import pytest
from mypkg.config import settings

@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    """Forces usage of [testing] env from `settings.toml` for tests"""
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")
  
