# Flip a dict, so the keys become values and vice versa.

d = {'a': 1, 'b': 2, 'c': 3}

flipped_dict = {value : key
                for key, value in d.items()}

print(flipped_dict)
