import pathlib
import logging

from platformdirs import user_config_dir
from moderngl_playground.settings.settings import Settings


logger = logging.getLogger(__name__)


def load_settings() -> Settings:
    """Load settings from config file"""
    config_path = pathlib.Path(user_config_dir(
        "moderngl-playground")) / "config.json"
    if not config_path.exists():
        logger.info("Config not exist, creating the default config.")
        settings = Settings()
        save_settings(settings)
    else:
        logger.info(f"Loading config from {config_path}.")
        with open(config_path, "r") as config_file:
            config_json = config_file.read()
            settings = Settings.schema().loads(config_json)
    return settings


def save_settings(settings: Settings):
    config_dir = pathlib.Path(user_config_dir(
        "moderngl-playground"))
    if not config_dir.exists():
        logger.info(
            f"Config directory {config_dir} doesn't exist, creating for the first time.")
        config_dir.mkdir(parents=True)
    config_path = config_dir / "config.json"
    config_json: str = settings.to_json()
    with open(config_path, "w") as config_file:
        config_file.write(config_json)