from collections import Counter
def top_10_most_common_words(text: str) -> dict[str, int]:
    most_common = {}
    new_text = text.replace("\n\n", " ")
    new_text = new_text.replace("\n", " ")
    new_text = new_text.lower()
    punctuation_marks = [",", ".", "?", "-", '"', "!", ":"]

    for mark in punctuation_marks:
        new_text = new_text.replace(mark, "")
    words = new_text.split(" ")
    
    for word in words:
        if len(word) >= 3:
            if most_common.get(word, "default") == "default":
                most_common[word] = 1
            else:
                most_common[word] = most_common[word] + 1
    most_common = Counter(most_common)
    most_common = dict(sorted(most_common.items(), key = lambda item: (-item[1], item[0])))
    most_common = dict(list(most_common.items())[:10])
    
    return most_common
