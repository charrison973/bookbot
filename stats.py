def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def get_word_count(filepath):
    file_contents=get_book_text(filepath)
    number_of_words = len(file_contents.split())
    return number_of_words

def get_character_count(filepath):
    all_characters = {}
    file = open(filepath, 'r')
    for line in file:
        for word in line.lower():
            for character in word:
                if character not in all_characters:
                    all_characters[character] = 1
                else:
                    all_characters[character] +=1
    return all_characters

def get_sorted_characters(filepath):
    characters = get_character_count(filepath)
    sorted_list = sorted(characters.items(), key=lambda x: x[1], reverse = True)
    for line in sorted_list:
        if line[0].isalpha():
            print(line[0]+": "+str(line[1]))
    return sorted

def sort_on(dict):
    return dict["num"]