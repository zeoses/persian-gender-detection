# Persian Gender Detection

A simple python package to detect gender by Persian first name. (With more than 19K names)

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

# Detect gender
get_gender('  عــــلی  ')         # MALE
get_gender('نرگـــ😉ــس')         # FEMALE
get_gender('حســ😎ــن')           # MALE
get_gender('۱۲۳۹۹۳محمدعلی123')    # MALE
get_gender('۱۲۳مهناز۱۲۳')         # FEMALE
get_gender('فاطمه زهرا')          # UNKNOWN
get_gender('فاطمه زهرا', 
          find_nearest_name=True) # (FEMALE, 'فاطمه')
get_gender('محمدنیسنممدیتیس', 
          find_nearest_name=True) # ('MALE', 'محمد')

```
Changelog
------
1.2.1
* Fixed issues in two-part names and added find_nearst_name flag to find and return the nearest name. 

1.1.0  
* Increasing the dataset of names from 6k to 19k
* convert names dataset from JSON to Python dictionary
* If a name does not exist in the dataset, it finds the gender in two-part names using the first part.  

1.0.5
* First version with 6k name dataset

Issues
------

Feel free to submit issues and enhancement requests.

Contributing
------------

Please feel free to contribute names database with your kindly pull requests.

License
------------
Licensed under [MIT License](LICENSE)
