from functools import lru_cache
import os
from pydantic import BaseSettings


class Config(BaseSettings):
    HEADLESS: bool = True


class DevelopmentConfig(Config):
    pass


class JenkinsConfig(Config):
    pass


def get_config_name():
    return os.getenv("TEST_CONFIG") or "default"


def get_config(config_name="default"):
    configs = {
        "development": DevelopmentConfig(),
        "jenkins": JenkinsConfig(),
        "default": JenkinsConfig(),
    }
    return configs[config_name]