from setuptools import setup

with open('./README.md', 'r') as f:
    readme = f.read()

setup(
    name='persian-gender-detection',
    version='1.2.1',
    packages=['persian_gender_detection'],
    include_package_data=True,
    data_files=[('', [
        'persian_gender_detection/gender/iranianNamesDataset.py',
        'persian_gender_detection/gender/iranianNamesDataset.csv',
    ])],
    url='https://github.com/zeoses/persian-gender-detection',
    license='MIT License',
    author='Mehraban',
    description='A simple python package to detect gender by Persian first name. (With more than 19K names).',
    long_description=readme,
    long_description_content_type='text/markdown',
    keywords='persian-gender-detection, farsi gender, iranian gender, name gender, persian gender detection, gender detection',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Persian',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Localization'
    ],
    project_urls={
        'Source': 'https://github.com/zeoses/persian-gender-detection',
        'Documentation': 'https://github.com/zeoses/persian-gender-detection',
    },
)
