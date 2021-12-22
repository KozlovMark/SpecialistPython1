# Дана строка текста, слова разделены пробелами.
# В предложении могут присутствовать следующие знаки препинания ",.!?-". Знаки препинания частьюслова не являются.
# Определить в предоставленном сообщении количество слов длиной больше, чем 7.

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam placerat consequat vestibulum. " \
       "Donec tincidunt sed lorem et feugiat. Nullam elementum"
# Примечание: для генериации текста можете воспользоваться сайтом: https://ru.lipsum.com/
# Примечание: обратите внимание на перенос длинной строки на новую строку

i = 0
symbol = 0
word = 0
length_string = len(text)

while i < length_string:
    if text[i] != " " and text[i] != "." and text[i] != "," and text[i] != "!" and text[i] != "?" and text[i] != "-":
        symbol += 1
    else:
        symbol = 0
    if symbol == 8:
        word += 1
    i += 1
print("Number of words per line =", word)
