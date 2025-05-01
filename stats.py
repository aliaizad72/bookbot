def word_count(str):
    return len(str.split())

def char_count_dict(str):
    dict = {}
    for char in str:
        key = char.lower()
        if char.lower() in dict:
            dict[key] += 1
        else:
            dict[key] = 1
    return dict

def char_sort_by_count(dict):
    sorted = []
    for k,v in dict.items():
        if k.isalpha():
            sorted.append({ "char": k, "count": v})
        else:
            continue
    sorted.sort(key=lambda dict: dict['count'], reverse=True)
    return sorted


