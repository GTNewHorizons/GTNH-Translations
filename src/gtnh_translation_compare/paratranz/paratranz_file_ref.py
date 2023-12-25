from typing import Dict, Any

from paratranz_client import File


class ParatranzFileRef:
    def __init__(self, value: File, extra: Dict[str, Any]):
        self.value = value
        self.extra = extra
