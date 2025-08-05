"""Configuration management utilities."""

from pathlib import Path
from typing import Any, Dict

import yaml


DEFAULT_PATH = Path(__file__).resolve().parent.parent / "config.yaml"


def load_config(path: str | Path = DEFAULT_PATH) -> Dict[str, Any]:
    """Load configuration from a YAML file.

    Args:
        path: Path to the configuration file.

    Returns:
        Parsed configuration as a dictionary.
    """
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}
