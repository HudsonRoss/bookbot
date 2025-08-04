def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents


def word_count(filepath):
    word_list = get_book_text(filepath).split()
    return len(word_list)


def char_count(filepath):
    char_dict = {}
    text = get_book_text(filepath)
    text_lower = text.lower()
    chars = list(text_lower)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for current_letter in alphabet:
        current_letter_list = []
        current_letter_list = [current_letter for char in chars if char == current_letter]
        char_dict[current_letter] = len(current_letter_list)
    return char_dict


