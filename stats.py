
def get_book_text(filepath):
    with open(filepath, "r") as f:
        file_string = f.read()
    return file_string
def count_words(filepath):
    count = 0
    with open(filepath, "r") as file:
        word_list = file.read().split()
        count = len(word_list)
    return count

def count_characters(file_string):
    funnyList = []
    list_index_dict = {}
    count = 0
    for char in file_string:
        if char.lower() not in list_index_dict and char.isalpha():
            list_index_dict[char.lower()] = count
            count+=1;
            funnyList.append({f'{char.lower()}': ord(char.lower()) - ord('a'), "num": 0 })
        if char.lower() in list_index_dict:
            funnyList[list_index_dict[char.lower()]]["num"]+=1
    print(list_index_dict)
    return funnyList
