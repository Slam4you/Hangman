from random import *

def is_invalid(letter):
    while True:
        if letter in 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' and len(letter) == 1:
            return False
        else:
            print('Rus letter, please')
            return True

def get_word():
    word_list = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ',
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА',
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК',
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН',
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН',
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР',
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК',
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА',
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']
    word = choice(word_list)
    return word.upper()

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |
           |
           |
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |
           |
           |
           |
           -
        '''
    ]
    return print(stages[tries])


def game(word):
    print('Wants to play a game, deadman? !!!only rus symbols!!!')
    tries = 6
    word_completion = []
    [word_completion.append('_') for i in range(len(word))]
    guessed_letters = []  # список уже названных букв

    while tries != 0:
        display_hangman(tries)
        print(*word_completion)
        print('Write letter')
        char = input().upper()
        print()
        if is_invalid(char):
            continue
        if char in guessed_letters:
            print('Already searched, try another one')
            continue
        if char in word:
            guessed_letters.append(char)
            word_dubl = word
            for _ in range(word.count(char)):
                word_completion[word_dubl.find(char)] = char
                word_dubl = word_dubl.replace(char,'*', 1)
            if '_' not in word_completion:
                print('The word was', '"',word, '"')
                print('Well done, you used', len(guessed_letters), 'letters to win')
                break
        else:
            guessed_letters.append(char)
            tries -= 1
    if tries == 0:
        display_hangman(tries)
        print('Sorry bro, you are dead...')
        print('The word was', '"',word, '"')

pl_again = True
while pl_again:
    game(get_word())
    print('Another try? (д/н)')
    if input() != 'д':
        pl_again = False