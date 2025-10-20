def get_num_of_words(file_contents):
    words = file_contents.split()
    return len(words)

def get_nums_of_chars(text):
    char_dict = {}
    text = text.lower()

    for ch in text:
        if ch in char_dict:
            char_dict[ch] += 1

        else:
            char_dict[ch] = 1

    return char_dict

def sort_on(item):
    return item[1]

def sort_dict(char_dict):
    char_dict_list = []

    for c in char_dict:
        char_dict_list.append((c, char_dict[c]))

    char_dict_list.sort(reverse=True, key=sort_on)

    return char_dict_list
