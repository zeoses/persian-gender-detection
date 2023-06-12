import os
import re
import json
from .gender.iranianNamesDataset import names


def clean_name(name:str) -> str:
    pattern = '^\s+|^0-9+|^۰-۹|[^(آ-ی)(a-z)]+'

    replacements = {
        "ي": "ی",
        "ك": "ک",
        "ـ": "",
        "\َ": "",
        "\ِ": "",
        "\ُ": "",
        "\ً": "",
        "\ٍ": "",
        "\ٌ": "",
        "\ْ": "",
        "\ْ": "",
    }

    name = name.lower()
    name = "".join([replacements.get(c, c) for c in name])
    name = re.sub(pattern, '',name)
    return name


def get_gender(name:str) -> str:
    name = clean_name(name)
    name = name.replace("آ", "ا").replace(" ", "")

    if name in names:
        return 'MALE' if names[name] == 'M' else 'FEMALE'
    else:
        for i in range(max(len(name), 8), 2, -1):
            if name[:i] in names:
                return 'MALE' if names[name[:i]] == 'M' else 'FEMALE'

    return 'UNKNOWN'


