from stats import get_number_of_words, get_number_of_characters,sort_dictionary
import sys

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    text = get_book_text(sys.argv[1])
    number_of_words = get_number_of_words(text)
    #print(f"{number_of_words} words found in the document")
    number_of_characters = get_number_of_characters(text)
    # for char in number_of_characters:
    #     print(f"'{char}': {number_of_characters[char]}")
    ordenados = sort_dictionary(number_of_characters)

    #print(ordenados)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print("Found 75767 total words")
    print("--------- Character Count -------")
    for char in ordenados:
        if not char['char'].isalpha():
            continue

        print(f"{char['char']}: {char['num']}")

main()