import os.path
from uuid import uuid1
import datetime


def upload_adv_photo(instance, filename: str) -> str:
    ext = filename.split(".")[-1]
    return os.path.join(str(instance.categories.value),
                        str(datetime.datetime.strftime(instance.created_at, "%d_%m_%Y")),
                        instance.title,
                        f"__{uuid1()}.{ext}")
