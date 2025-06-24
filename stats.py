def get_number_of_words(text):
    words = text.split()
    return len(words)

def get_number_of_characters(text):
    chars_dictionary = dict()
    for char in text.lower():
        if char in chars_dictionary:
            chars_dictionary[char] += 1
        else:
            chars_dictionary[char] = 1
    return chars_dictionary

def sort_dictionary(chars_dictionary):
    sorted_dict = dict()
    dict_list = []

    for key in chars_dictionary:
        dict_list.append(dict(char= key, num = chars_dictionary[key]))

    dict_list.sort(reverse=True, key=sort_on)

    return dict_list

def sort_on(items):
    return items["num"]