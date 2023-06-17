from typing import Literal

from .gender.iranian_names_dataset import names

GENDER = Literal["MALE", "FEMALE", "UNKNOWN"]


def clean_name(name: str) -> str:
    persian_characters = set("آابپتثجچحخدذرزژسشصضطظعغفقکگلمنوهی")

    replacements = str.maketrans(
        {
            "ي": "ی",
            "ك": "ک",
            "آ": "ا",
        }
    )

    name = name.lower().translate(replacements)
    return "".join([char for char in name if char in persian_characters])


def get_gender(name: str) -> GENDER:
    name = clean_name(name)
    if name in names:
        return "MALE" if names[name] == "M" else "FEMALE"

    return "UNKNOWN"


def get_gender_nearest(name: str) -> tuple[GENDER, str | None]:
    name = clean_name(name)
    if name in names:
        return ("MALE", name) if names[name] == "M" else ("FEMALE", name)

    for i in range(max(len(name), 8), 2, -1):
        part = name[:i]
        if part in names:
            return ("MALE", part) if names[part] == "M" else ("FEMALE", part)

    return "UNKNOWN", None
