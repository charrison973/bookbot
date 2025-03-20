import sys
from stats import *

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = sys.argv[1]
    num_words = get_word_count(book)
    # print(get_character_count("books/frankenstein.txt"))
    
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    get_sorted_characters(book)
    print("============= END ===============")

if __name__ == "__main__":
    main()