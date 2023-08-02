
'''
В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. \n
Не учитывать знаки препинания и регистр символов. \n
За основу возьмите любую статью из википедии или из документации к языку.
'''


WORK_TEXT = "— Скажи-ка, дядя, ведь недаром "\
"Москва, спаленная пожаром,"\
"Французу отдана?" \
"Ведь были ж схватки боевые," \
"Да, говорят, еще какие!" \
"Недаром помнит вся Россия" \
"Про день Бородина!" \

"— Да, были люди в наше время," \
"Не то, что нынешнее племя:" \
"Богатыри — не вы!" \
"Плохая им досталась доля:" \
"Немногие вернулись с поля…" \
"Не будь на то господня воля," \
"Не отдали б Москвы!" \

FREQUENT_COUNT = 10
def most_frequent_words(text: str, count_words: int) -> dict:
    words_list = text.upper() \
        .replace(".", " ") \
        .replace(",", " ") \
        .replace(";", " ") \
        .replace(":", " ") \
        .replace("!", " ") \
        .replace("?", " ") \
        .replace(" - ", " ") \
        .split()
    words_count = {}
    for w in words_list:
        words_count[w] = words_list.count(w)
    return dict(sorted(words_count.items(), key=lambda item: item[1], reverse=True)[:count_words])


def main():
    for i, w in enumerate(most_frequent_words(WORK_TEXT, FREQUENT_COUNT).items(), 1):
        print(f"{i:2}. {w[0]:<10} - {w[1]}")


if __name__ == "__main__":
    main()
