# gdict = {'a': 1, 'b': 2, 'c': {'x': 24, 'y': 25, 'z': 26}, 'd': 4}
#
# mydict = {}
# for i, j in gdict.items():
#     if not type(j) == dict:
#         mydict.update({i: j})
#     else:
#         value_of_p = len(j)
#         mydict.update({i: value_of_p})
#         mydict.update(j)
#
# print(mydict)

# gdict = {'a': 1,
#          'c': {'a': 2,
#                'b': {'x': 5,
#                      'y': 10}},
#          'd': [1, 2, 3]}
#
# mydict = {}
#
# for i, j in gdict.items():
#     if not type(j) == dict:
#         mydict.update({i: j})
#     else:
#
# print(mydict)

# def flatten_dict(gdict, separator='_', prefix=''):
#     x = {prefix + separator + k if prefix else k: v
#          for i, j in gdict.items()
#          for k, v in flatten_dict(j, separator, i).items()
#          } if isinstance(gdict, dict) else {prefix: gdict}
#
#     return x

# def flatten_dict(mydict, separator='_', prefix=''):
#     mod_dict = {prefix + separator + k if prefix else k: v
#                 for i, j in mydict.items()
#                 for k, v in flatten_dict(j, separator, i).items()} \
#         if isinstance(mydict, dict) else {prefix: mydict}
#     return mod_dict

#
# def flatten_dict(mydict, separator='_', prefix=''):
#     mod_dict = {prefix + separator + k if prefix else k: v
#                 for i, j in mydict.items()
#                 for k, v in flatten_dict(j, separator, i).items()} \
#         if isinstance(mydict, dict) else {prefix: mydict}
#     return mod_dict
# def flatten_dict(mydict, separator='_', prefix=''):
#     x = {prefix + separator + k if prefix else k: v
#          for i, j in mydict.items()
#          for k, v in flatten_dict(j, separator, i).items()} \
#         if isinstance(mydict, dict) else {prefix: mydict}

#

# def flatten_dict(mydict, separator='_', prefix=''):
#     items = []
#     for k, v in mydict.items():
#         new_key = prefix + separator + k if prefix else k
#         if isinstance(v, dict):
#             items.extend(flatten_dict(v, separator, k).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)

# def flatten_dict(mydict, separator='_', prefix=''):
#     items = []
#     for k, v in mydict.items():
#         new_key = prefix + separator + k if prefix else k
#         if isinstance(v, dict):
#             items.extend(flatten_dict(v, separator, k).items())
#         else:
#             items.append((new_key, v))
#     return dict(items)

def flatten_dict(mydict, separator='_', prefix=''):
    mod_dict = {prefix + separator + k if prefix else k: v
                for i, j in mydict.items()
                for k, v in flatten_dict(j, separator, i).items()}\
        if isinstance(mydict, dict) else {prefix: mydict}
    return mod_dict


ini_dict = {'geeks': {'Geeks': {'for': 7}},
            'for': {'geeks': {'Geeks': 3}},
            'Geeks': {'for': {'for': 1, 'geeks': 4}}}

print(flatten_dict(ini_dict))
gdict = {'a': 1, 'b': 2, 'c': {'x': 24, 'y': 25, 'z': 26}, 'd': 4}
print(flatten_dict(gdict))


