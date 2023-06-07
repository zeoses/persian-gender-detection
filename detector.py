import json
import re
from pathlib import Path
import os

base_path = str(Path(os.getcwd()))
with open(base_path+'/gender/male.json') as male_file:
    male = json.loads(male_file.read())

with open(base_path+'/gender/female.json') as female_file:
    female = json.loads(female_file.read())


def clean_name(name:str) -> str:
    pattern = '^\s+|^0-9+|^۰-۹|[^(آ-ی)(a-z)]+'

    replacements = {
        'ی': 'ی', 'ك': 'ک', 'ـ': '',
        '\َ': '', '\ِ': '', '\ُ': '',
        '\ً': '', '\ٍ': '', '\ٌ': '', '\ْ': '',
    }

    name = name.lower()
    name = "".join([replacements.get(c, c) for c in name])
    name = re.sub(pattern, '',name)
    return name


def get_gender(name:str) -> str:
    name = clean_name(name)
    if male.get(name, False):
        return 'MALE'
    elif female.get(name, False):
        return 'FEMALE'
    else:
        return 'UNKNOWN'


