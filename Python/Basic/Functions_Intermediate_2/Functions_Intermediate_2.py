# Assignment: Functions Intermediate II
# 1. Update Values in Dictionaries and Lists
x = [[5, 2, 3], [10, 8, 9]]
x[1][0] = 15
print(x)

students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
students[0]["last_name"] = "Bryant"
print(students)


sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory["soccer"][0] = "Andres"
print(sports_directory)

z = [{'x': 10, 'y': 20}]
z[0]["y"] = 30
print(z)

# 2. Iterate Through a List of Dictionaries
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]


def key_and_value(list):
    for val in list:
        print(
            f"first_name - {val['first_name']}, last_name - {val['last_name']}")


key_and_value(students)

# 3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for val in some_list:
        print(f"{val[key_name]}")


print(iterateDictionary2("last_name", students))

# 4.Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(list):
    for key in list:
        print(f"{len(list[key])}")
        for val in list[key]:
            print(val)
        print("")


printInfo(dojo)