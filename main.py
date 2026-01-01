import sys

from stats import char_count, num_key, word_count, sort_on, report

def main():

    if (len(sys.argv) < 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = str(sys.argv[1])
    num_chars = char_count(book_path)
    num_words = word_count(book_path)
    sorted_counts = sort_on(num_chars, num_key)
    report(sorted_counts, book_path, num_words)

main()