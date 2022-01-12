# !/usr/bin/env python
import pymorphy2
import csv

# verbs = [counter, verb, aspect=D|N, adverb_pres=adv|0, adverb_past=adv]
#
# counter - порядковий номер слова
# verb - саме дієслово
# aspect - вид (доконаний - D, недоконаний - N)
# adverb_pres - дієприслівник теперішнього часу
# adverb_past - дієприслівник минулого часу


def write_in_file(verbs_list: list, name='adverbs.csv'):
    with open(str(name), 'a', encoding='utf-8') as text:
        writer = csv.writer(text, delimiter=';')
        writer.writerows(verbs_list)
    return


# noinspection SpellCheckingInspection
class Verbs:

    def __init__(self, verbs):
        self.verbs = verbs

    morph = pymorphy2.MorphAnalyzer(lang='uk')

# in: list of str ['', '']
# out: list of lists of str ([['', ''], ['']])
    @staticmethod
    def operate_file(row: str):
        row = row.strip('\n')

        if ';' in row:
            row = row.split(';')
        elif ',' in row:
            row = row.split(',')
        elif '\t' in row:
            row = row.split('\t')
        else:
            row = [row]

        return row

# in: ONLY FOR list of lists of str ([['']]), BUT with bare verbs
# out: list of lists of str ([['counter', 'verb', 'aspect=D|N']])
    @staticmethod
    def characteristics(row: list, counter: int, morph=pymorphy2.MorphAnalyzer(lang='uk')):
        word = row[0]
        verb = morph.parse(word)[0]

        aspect = verb.tag.aspect
        # noinspection SpellCheckingInspection
        if verb.tag.POS == "VERB" and aspect == 'perf':
            aspect = 'D'
        else:
            aspect = 'N'

        row = [str(counter), word, aspect]
        return row

    @staticmethod
    def present_exception(verb: str):
        if verb[-3:] == 'ити':
            adverb_pres = verb[:-3] + 'ячи'
        elif verb[-4:] == 'вати':
            adverb_pres = verb[:-4] + 'ючи'
        elif verb[-3:] == 'ати':
            adverb_pres = verb[:-2] + 'ючи'
        else:
            adverb_pres = None

        return adverb_pres

    @staticmethod
    def postfix_method(verb: str, postfix=bool):
        if postfix is False or postfix is True:
            return verb
        elif verb[-2:] == 'ся' or verb[-2:] == 'сь':
            postfix = True
            verb = verb[:-2]
        else:
            postfix = False

        return verb, postfix

# in: list of lists of str (['counter', 'verb', 'aspect=D|N', 'conjugation=1|2]')
# out: list of lists ([counter, verb, aspect=D|N|None, adverb_pres=adv|None, adverb_past=adv])
    # noinspection PyUnboundLocalVariable
    def verb2adverb(self, morph=pymorphy2.MorphAnalyzer(lang='uk')):
        self.verbs = self.verbs[1:]
        counter = 0

        for row in range(len(self.verbs)):
            self.verbs[row] = self.operate_file(self.verbs[row])
            counter += 1

            if len(self.verbs[row]) == 1:
                self.verbs[row] = self.characteristics(self.verbs[row], counter)
            else:
                self.verbs[row] = self.verbs[row][:3]

            verb = self.verbs[row][1]

            sliced_verb, postfix = self.postfix_method(verb)
            if sliced_verb[-3:] == 'вти':
                adverb_past = sliced_verb[:-2] + 'ши'
            else:
                adverb_past = sliced_verb[:-2] + 'вши'
            if postfix:
                adverb_past = adverb_past + 'сь'

            verb = morph.parse(verb)[0]
            if self.verbs[row][2] == 'N':
                if verb.tag.POS == "VERB":
                    third_verb = verb.inflect({'plur', '3per'})[0]
                    third_verb, postfix = self.postfix_method(third_verb)
                    adverb_pres = third_verb[:-2] + 'чи'
                else:
                    self.verbs[row][1], postfix = self.postfix_method(self.verbs[row][1])
                    adverb_pres = self.present_exception(self.verbs[row][1])
                if postfix:
                    adverb_pres = adverb_pres + 'сь'
            else:
                adverb_pres = None

            self.verbs[row].append(adverb_pres)
            self.verbs[row].append(adverb_past)

        return self.verbs
