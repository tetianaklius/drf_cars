import os.path
from uuid import uuid1


def upload_adv_photo(instance, filename: str) -> str:
    ext = filename.split(".")[-1]
    return os.path.join(instance.title, f"__{uuid1()}.{ext}")

