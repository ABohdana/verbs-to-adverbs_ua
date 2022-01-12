# verbs-to-adverbs_ua
A program to automatically extract and analyse verbs of Ukrainian language and then to generate adverbs from them. Some ilustrative data included.

## What?
The repository includes:
* *verb2adverb* - program that iterates through CSV and TXT files with verbs in a given directory, launches adverbs generation, saves adverbs to a corresponding CSV file;
* *verbs_functions* - module with all the methods used for generation;
* *verbs_axtraction&analysis* - additional program that creates a CSV file with verbs out of a given TXT file with a list of verbs annotated for the Ukrainian Language Corpus;
* *data* - CSV files with suggested input verbs;
* *results* - output CSV files that include id, verb, its aspect (it determines whether a present tense adverb can be generated), present tense adverb, past tense adverb;
* *adverbs_forming_errors* - observed errors of adverb generation.

## Why?
This project was created as part of my Computational Linguist studies at the Taras Shevchenko University of Kyiv in the middle of the 2d grade.

## How?
### Technologies
* python 3.7
* pymorphy2
* pathlib
* csv

### Structure
The main program consists of two files: *verb2adverb* and *verbs_functions*. The first one calls the latter.

Here is an example flow of operate_file method in *verbs_functions*:
![operate_file function flow](operate_file%20function%20flow%20-%20ivahnenko.png)

### Setup
To use the program you need to run *verb2adverb.py* and enter a path to the directory containing files with verbs:
```
C:\path\to\file>python verb2adverb.py
Будь ласка, вкажіть шлях до файлів (з \\ для Windows): enter\\path\\to\\files\\with\\verbs
Adverbs were generated successfully.
```
You will get a *adverbs.csv* file in the program directory.

## Contact
Feel free to contact me via ivahnenko.bohdana@knu.ua
