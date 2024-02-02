################## Assignment Dhineshbabu ###################
# Date : 02/02/2024
################## Question 1 ####################
weekdays = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']


def converttostring(list_inp):
    joined_string = " - ".join(list_inp)
    return joined_string

print(converttostring(weekdays))

################## Question 2 ####################
days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sun', 'mon', 'mon']


def findMaxOccuringString(days):
    emptyDictionary = {}
    for x in days:
        emptyDictionary.setdefault(x, 0)
        emptyDictionary[x] += 1
    # Interchanging the keys and values inside the dictionary
    new_Dict = {}
    for keys, values in emptyDictionary.items():
        new_Dict[values] = keys
    # Extracting the numbers from the dictionary into a List
    Empty_List = []
    for keys, values in new_Dict.items():
        Empty_List.append(keys)
    # Picking the maximum appeared value from the input list
    return new_Dict[max(Empty_List)] + " is the highest occurring element"


res = findMaxOccuringString(days)
print(res)

################## Question 3 ####################

a = {'x': 1, 'y': 2, 'z': 3}
b = {'a': 4, 'b': 5, 'y': 6}


def dictMerge(a, b):
    c = {}
    # appending or updating the empty dictionary "c" with the values of dictionary "a"
    for key, value in a.items():
        c.setdefault(key, value)
    # appending or updating the empty dictionary "c" with the values of dictionary "b"
    # if the key already exists in the dictionary "c", then the values of that key will be added together
    for key, value in b.items():
        if key in c:
            c[key] += value
        else:
            c.setdefault(key, value)
    return c


res1 = dictMerge(a, b)
print(res1)

################## Question 4 ####################

items = [{'Delhi': 3}, {'Mumbai': 9}, {'Goa': 7}, {'Gujrat': 4}]


def itemWithHighestValue(items):
    dictionary1 = {}

    for instance in items:
        for key, value in instance.items():
            dictionary1.setdefault(key, value)

    dictionary2 = {}
    for keys, values in dictionary1.items():
        dictionary2[values] = keys

    emp3 = []
    for keys, values in dictionary2.items():
        emp3.append(keys)

    return dictionary2[max(emp3)]


result1 = itemWithHighestValue(items)
print(result1+" having the highest value")

################## Question 5 ####################

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}


def group_by_owners(files):
    hollowDictionary = {}
    for keys, values in files.items():
        if values not in hollowDictionary:
            hollowDictionary[values] = [keys]
        else:
            hollowDictionary[values].append(keys)

    return hollowDictionary


print(group_by_owners(files))