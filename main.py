import sys
from stats import get_num_of_words, get_nums_of_chars, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for ch, count in sorted_dict_list:
            if ch.isalpha():
                print(f"{ch}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
         print("Usage: python3 main.py <path_to_book>")
         sys.exit(1)
    
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    word_count = get_num_of_words(file_contents) 
    char_dict = get_nums_of_chars(file_contents)
    sorted_dict_list = sort_dict(char_dict)
    print_report(book_path, word_count, sorted_dict_list)

main()
