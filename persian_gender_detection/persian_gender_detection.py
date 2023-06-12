import os
import re
import json
from .gender.iranianNamesDataset import names


# base_path = os.path.dirname(__file__)

# # with open(base_path+'/gender/male.json', encoding="utf8") as male_file:
# #     male = json.loads(male_file.read())

# # with open(base_path+'/gender/female.json', encoding="utf8") as female_file:
# #     female = json.loads(female_file.read())

# with open(base_path+'/gender/iranianNamesDataset.json', encoding="utf8") as male_file:
#     names = json.loads(male_file.read())

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


