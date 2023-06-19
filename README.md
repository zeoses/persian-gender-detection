# Persian Gender Detection

A simple python package to detect gender by Persian first name. (With more than 19K names)

for this package i use this [repo](https://github.com/peymanslh/persian-gender-detection/) if you are use NPM that's great choice.

User guide
----------

### Installation


Install with PIP:

```bash
$ pip install persian-gender-detection
```
### get_gender
this function works for finding gender and returning gender. if find the gender return it, otherwise return `UNKNOWN`
#### Example

```python
from persian_gender_detection import get_gender

# Detect gender
get_gender('  عــــلی  ')             # MALE
get_gender('نرگـــ😉ــس')             # FEMALE
get_gender('حســ😎ــن')               # MALE
get_gender('۱۲۳۹۹۳محمدعلی123')        # MALE
get_gender('۱۲۳مهناز۱۲۳')             # FEMALE
get_gender('فاطمه زهرا')              # UNKNOWN
get_gender("جانان")                   # UNKNOWN
```
### get_gender_nearest
sometimes is difficult to find the gender from names, this problem can have many reasons for example 2 parts names or mistakes in writing. This function helps to solve this problem to some extent.
#### Example
```python
from persian_gender_detection import get_gender_nearest

get_gender_nearest('فاطمه زهرا')      # (FEMALE, 'فاطمه')
get_gender_nearest('محمدنیسنممدیتیس') # ('MALE', 'محمد')
get_gender_nearest("جانان")           # ("FEMALE", "جانا")

```

Changelog
------ 
1.4.0
first, thanks to [amirsoroush](https://github.com/amirsoroush) for the changes and improvement code, in this (PR)[https://github.com/zeoses/persian-gender-detection/pull/2] you can see all of the changes. But in summary, the following has been done:
* improve and simplify code and formatting, remove unused packages.
* Adding a new function for finding the nearest name and removing the find_nearst_name flag for better output.

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
