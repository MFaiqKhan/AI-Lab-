
dict = {}

print(dir(dict))

print(help(dict.update))


# simple func for adding key value pairs to a dictionary
def add_to_dict(key, value):
    dict[key] = value
    return dict

# simple func for updating key value pairs in a dictionary
def update_dict(key, value):
    dict.update({key: value})
    return dict

# simple func for deleting key value pairs in a dictionary
def delete_from_dict(key):
    del dict[key]
    return dict

# func for word count
def word_count(string):
    dict = {}
    for word in string:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

words = ['physics', 'maths', 'physics']

print(word_count(words))
