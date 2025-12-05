def numwords(content):
    words = content.split()
    num_of_words = len(words)
    return num_of_words


def numchar(content):
    chars = {}
    for i in content:
        key = i.lower()
        chars[key] = chars.get(key, 0) + 1
    return chars


def dic_list(chars):
    char_list = []
    for key, num in chars.items():
        if key.isalpha():
            char_dic = {}
            char_dic["char"] = key
            char_dic["num"] = num
            char_list.append(char_dic)
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

