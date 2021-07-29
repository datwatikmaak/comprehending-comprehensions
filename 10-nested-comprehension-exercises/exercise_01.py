# Given this sort of dict `(country:city-list)`:
# {'Israel': ['Jerusalem', 'Tel Aviv'],
# 'USA': ['Boston', 'New York', 'Chicago'],
# 'China': ['Beijing', 'Shanghai']}

# Use a nested list comprehension to produce a list of tuples that look like (city, country).
places = {
    'Israel': ['Jerusalem', 'Tel Aviv'],
    'USA': ['Boston', 'New York', 'Chicago'],
    'China': ['Beijing', 'Shanghai']
}

result = [
    (one_city, country)
    for country, all_cities in places.items()
    for one_city in all_cities
]

print(result)
