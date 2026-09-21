import json
from datetime import datetime, date, time
from typing import Any, Callable


class TimeAwareEncoder(json.JSONEncoder):

    def default(self, o: Any) -> Any:
        if isinstance(o, (datetime, date, time)):
            return o.isoformat()
        return super().default(o)


class TimeAwareDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.time_aware_decode, *args, **kwargs)

    def time_aware_decode(self, dct):
        for k, v in dct.items():
            if isinstance(v, str):
                try:
                    # thử parse datetime
                    return {k: datetime.fromisoformat(v)}
                except ValueError:
                    try:
                        # thử parse date
                        return {k: date.fromisoformat(v)}
                    except ValueError:
                        try:
                            # thử parse time
                            return {k: time.fromisoformat(v)}
                        except ValueError:
                            pass
        return dct
