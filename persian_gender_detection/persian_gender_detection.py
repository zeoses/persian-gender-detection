from .gender.iranianNamesDataset import names


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


def get_gender(name: str, find_nearest_name: bool = False) -> str:
    name = clean_name(name)

    if name in names:
        if find_nearest_name:
            return ("MALE", name) if names[name] == "M" else ("FEMALE", name)
        return "MALE" if names[name] == "M" else "FEMALE"

    elif find_nearest_name:
        for i in range(max(len(name), 8), 2, -1):
            if name[:i] in names:
                return (
                    ("MALE", name[:i])
                    if names[name[:i]] == "M"
                    else ("FEMALE", name[:i])
                )

    return "UNKNOWN"
