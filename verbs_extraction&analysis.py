#!/usr/bin/env python
#-*- coding: utf-8 -*-
import csv
import pymorphy2
morph = pymorphy2.MorphAnalyzer(lang='uk')

def verb_extraction(file, output_file='input_verbs_ivahnenko.csv'):
    with open(file, "r", encoding='utf-8') as verbs:
        verbs = verbs.readlines()
    
    words = []
    start = 5
    for verb in verbs:
        end = verb.find(',')
        words.append(verb[start:end].strip('1'))

    output_verbs = '\n'.join([w for w in words])

    with open(output_file, 'w') as text:
        text.write(output_verbs)

    return output_file


def verb_analisys(file, output_file='input_verbs_ivahnenko_extended.csv'):
    verbs = []

    with open(file, encoding='utf-8') as text:
        reader = csv.reader(text)
        for word in text:
            verbs.append(word)

    verbs = verbs[:-1]
    for verb in range(len(verbs)):
        verbs[verb] = verbs[verb].strip('\n')

    output_verbs = [['Номер', 'Дієслово', 'Вид', 'Перехідність', 'Дієвідміна']]
    vyd = None
    pereh = None
    diyev = None
    counter = 0

    for verb in range(len(verbs)):
        counter += 1
        p = morph.parse(verbs[verb])[0]
        if p.tag.POS != 'VERB':
            print(verbs[verb])
            continue

        vyd = p.tag.aspect
        if vyd == 'perf':
            vyd = 'D'
        elif vyd == None:
            vyd = '-'
        else:
            vyd = 'N'

        pereh = p.tag.transitivity
        if pereh == 'intr':
            pereh = 'P'
        elif pereh == None:
            pereh = '-'
        else:
            pereh = 'E'

        person = p.inflect({'plur','3per'})[0]
        if person[-3:] == 'уть' or person[-3:] == 'ють':
            diyev = 1
        elif person[-3:] == 'ать' or person[-3:] == 'ять':
            diyev = 2
        else:
            diyev = '-'

        lst = [str(counter), verbs[verb], vyd, pereh, str(diyev)]
        output_verbs.append(lst)

        with open(output_file, 'w', encoding='utf-8') as text:
        adv_writer = csv.writer(text, delimiter=',')
        for line in output_verbs:
            adv_writer.writerow(line)

    return output_verbs


if __name__ == '__main__':
    file_name = input("Please, enter the name of the file with unextracted verbs: ")
    verb_analisys(verb_extraction(file_name))
    print("Verbs are successfully extracted and analised. The results of each stage is saved to a .csv file.")
