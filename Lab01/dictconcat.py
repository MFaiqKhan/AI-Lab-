
def concat_dict(dict1, dict2):
    # dict3 = dict1.copy() 
   #  dict3.update(dict2)
    dict3 = {**dict1, **dict2}
    return dict3

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

print(concat_dict(dict1, dict2))