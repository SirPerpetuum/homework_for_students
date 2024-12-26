import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SPLIT_SYMBOL = '.\n'


def get_article(path: str) -> str:
    with open(path, 'r') as file:
        file_article = file.read()
    return file_article


def get_correct_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'correct_article.txt'))


def get_wrong_article() -> str:
    return get_article(os.path.join(BASE_DIR, '4_safe_text', 'articles', 'wrong_article.txt'))


def recover_article() -> str:
    wrong_article = get_wrong_article()
    new_article = wrong_article.split("\n")
    new_article.remove(new_article[4])
    new_wrong_article = ""
    for sentence in new_article:
        new_sentence = sentence.replace("!", "")
        new_sentence = new_sentence[::-1]
        new_sentence = new_sentence.replace(".", "")
        new_sentence = new_sentence.lower()
        new_sentence = new_sentence.replace("woof-woof", "cat")
        new_sentence = new_sentence.capitalize()
        new_wrong_article = new_wrong_article + new_sentence + ".\n"
    return new_wrong_article
