from cs50 import get_string


def main():
    text = get_string("Text: ")

    letters = count_letters(text)
    words = count_words(text)
    sentences = count_sentences(text)

    calculate_reading_level(letters, words, sentences)


def count_letters(text):
    letter_count = 0
    for i in range(len(text)):
        if text[i].isalpha and not text[i] == " " and not is_punct(text[i]) and not text[i] == "," and not text[i] == "'":
            letter_count += 1

    return letter_count


def count_words(text):
    word_count = text.count(" ") + 1

    return word_count


def count_sentences(text):
    sentence_count = 0
    for i in range(len(text)):
        if is_punct(text[i]):
            sentence_count += 1

    return sentence_count


def calculate_reading_level(letters, words, sentences):
    L = letters / words * 100
    S = sentences / words * 100
    index = 0.0588 * L - 0.296 * S - 15.8

    index = round(index)

    if index > 16:
        print("Grade 16+")
    elif index < 1:
        print("Before Grade 1")
    else:
        print(f"Grade {index}")


def is_punct(character):
    if character == "." or character == "?" or character == "!":
        return True


main()