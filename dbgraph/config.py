from __future__ import annotations

import json
from json import JSONDecodeError
from dataclasses import asdict, dataclass
from pathlib import Path


@dataclass
class Config:
    """Load and save configurations"""

    METADATA_URI: str | None = None
    OPENAI_BASE_URL: str | None = None
    MODEL: str | None = None
    API_KEY: str | None = None
    SOURCE_DATABASE_TYPE: str = "sql"

    @staticmethod
    def get_config_path() -> Path:
        path = Path.home() / ".dbgraph" / "config.json"
        if not path.parent.exists():
            path.parent.mkdir(parents=True, exist_ok=False)
        if not path.exists():
            path.touch(exist_ok=False)
        return path

    @classmethod
    def load(cls) -> Config:
        path = Config.get_config_path()
        try:
            with path.open("r") as f:
                data = json.load(f)
                config = cls(**data)
            return config
        except JSONDecodeError:
            config = cls()
            config.save()
            return config

    def save(self):
        path = Config.get_config_path()
        with path.open("w") as f:
            json.dump(asdict(self), f)
