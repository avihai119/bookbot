from stats import get_num_of_words, get_nums_of_chars, sort_dict

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents



def main():
    path = "books/frankenstein.txt"
    file_contents = get_book_text(path)
    word_count = get_num_of_words(file_contents) 
    char_dict = get_nums_of_chars(file_contents)
    char_dict_list = sort_dict(char_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for ch, count in char_dict_list:
            if str(ch).isalpha():
                print(f"{ch}: {count}")
    print("============= END ===============")

main()
