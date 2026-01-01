def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents


def word_count(filepath):
    word_list = get_book_text(filepath).split()
    return len(word_list)


def char_count(filepath):
    list_of_dict = []
    
    text = get_book_text(filepath)
    text_lower = text.lower()
    chars = list(text_lower)
    alphabet = "abcdefghijklmnopqrstuvwxyzâêëô"
    for current_letter in alphabet:
        current_char_dict = {}
        current_letter_list = []
        current_letter_list = [current_letter for char in chars if char == current_letter]
        char_dict_char_pref = "char"
        char_dict_num_pref = "num"
        current_char_dict[char_dict_char_pref] = current_letter
        current_char_dict[char_dict_num_pref] = len(current_letter_list)
        list_of_dict.append(current_char_dict)
    return list_of_dict


def num_key(dict):
    return dict.get("num", None)
    
def sort_on(list_of_dictionaries, sort_func):
    list_of_dictionaries.sort(reverse=True, key=sort_func)
    return list_of_dictionaries

def report(sorted_list_of_dictionaries, file_path, word_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for dict in sorted_list_of_dictionaries:
        print(f"{dict.get("char")}: {dict.get("num")}")

    return None

# word_counts = word_count("./books/frankenstein.txt")
# char_counts = char_count("./books/frankenstein.txt")
# sorted_counts = sort_on(char_counts, num_key)
# report(sorted_counts, "./books/frankenstein.txt", word_counts)


