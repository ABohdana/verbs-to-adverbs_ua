# !/usr/bin/env python
from pathlib import Path
from pathlib import PurePosixPath
from pathlib import PurePath
from verbs_functions import Verbs, write_in_file

names = [['номер', 'дієслово', 'вид', 'дієприслівник від основи теперішнього часу', 'дієприслівник від основи чол.р. минулого часу']]
write_in_file(names)

folder = input("Будь ласка, вкажіть шлях до файлів (з \\\\ для Windows): ").strip(""""' """)
# folder = "C:\\PycharmProjects\\Programming_Fedorova\\2 курс\\adverbs_lab\\data"

for path in Path(folder).iterdir():
    if PurePosixPath(str(path)).suffix == '.csv' or PurePosixPath(str(path)).suffix == '.txt':

        try:
            current_file = open(path, "r", encoding='utf-8')
            verbs = current_file.readlines()
            current_file.close()

            verbs[0] = verbs[0].strip('\ufeff')

            spreadsheet = Verbs(verbs)
            adverbs = spreadsheet.verb2adverb()
            write_in_file(adverbs)

        except UnicodeDecodeError:
            print('Файл ' + PurePath(str(path)).name + ' має неприпустиме кодування, встановіть UTF-8.')

print("Adverbs were generated successfully.")
