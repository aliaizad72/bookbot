import sys
from stats import word_count, char_count_dict, char_sort_by_count

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    doc = get_book_text(path)
    char_count = char_count_dict(doc)
    str = f"""============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found {word_count(doc)} total words
--------- Character Count -------\n"""
    for count in char_sort_by_count(char_count):
        str += f"{count['char']}: {count['count']}\n"

    str += "============= END ==============="
    print(str)
    # print(char_count)

main()
