import os
import sys
import yaml
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

from pathlib import Path

config_folder = Path(__file__).resolve().parent.parent.parent / 'config'

with open(config_folder / "config.yaml", "r") as file:
    CONFIG = yaml.load(file, Loader=yaml.FullLoader)

ENV = os.environ.get("ENV", CONFIG["env"])
