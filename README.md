# Persian Gender Detection

A simple python package to detect gender by Persian first name. (With more than 6K names)

for this package i use this [repo](https://github.com/peymanslh/persian-gender-detection/) if you are use NPM that's great choice.

Installation
------
Install with PIP:

```bash
$ pip install persian-gender-detection
```

Example
------
```python
from persian_gender_detection import get_gender

// Detect gender
get_gender('  عــــلی  ');         // MALE
get_gender('نرگـــ😉ــس');         // FEMALE
get_gender('حســ😎ــن');          // MALE
get_gender('۱۲۳۹۹۳محمدعلی123');  // MALE
get_gender('۱۲۳مهناز۱۲۳');       // FEMALE
```

Issues
------

Feel free to submit issues and enhancement requests.

Contributing
------------

Please feel free to contribute names database with your kindly pull requests.

License
------------
Licensed under [MIT License](LICENSE)
