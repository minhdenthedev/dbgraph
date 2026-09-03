import datetime
import json
from typing import Any, Callable


class DateTimeEncoder(json.JSONEncoder):
    """Custom encoder for datetime"""

    def default(self, o: Any) -> Any:
        if isinstance(o, (datetime.date, datetime.datetime)):
            return o.isoformat()
        return super().default(o)


def datetime_parser(obj):
    for key, value in obj.items():
        if isinstance(value, str):
            try:
                # try parsing ISO format
                obj[key] = datetime.datetime.fromisoformat(value)
            except ValueError:
                try:
                    # if there is only date
                    obj[key] = datetime.date.fromisoformat(value)
                except ValueError:
                    pass
    return obj


class DateTimeDecoder(json.JSONDecoder):
    """Custom decoder for datetime"""

    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=datetime_parser, *args, **kwargs)
