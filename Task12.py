# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа. 5 6 -> 2 3

from math import sqrt
summa = int(input('Введите сумму двух чисел '))
multiplication = int(input('Введите произведение двух чисел '))

diskriminant = sqrt( (summa/2)**2 - multiplication)
print( int( summa/2 - diskriminant ), int( summa/2 + diskriminant ) )
