import os

words = {'variable': ['holds a value, can be int or str, no spaces', 'x = 256, name = Finley'],
        'print': ["prints whatever is inside the (), can concatenate with + or use % to insert, \ special characters for tab and newline", "print('this will print this')"],
        'title': ["capitalizes first char of string, related: upper, lower", "string.title()"],
        'upper': ["capitalizes whole string, related: title, lower", "string.upper()"],
        'lower': ["lowercases whole string, related: upper, title", "string.lower()"],
        'strip': ["strips whitespace from string, related: rstrip, lstrip", "string.strip()"],
        'rstrip': ["strips whitespace from right of string, related: strip, lstrip", "string.rstrip()"],
        'lstrip': ["strips whitespace from left of string, related: strip, lstrip", "string.lstrip()"],
        'string': ["turn an int into a str", "str(124)"],
        'list': ["a collection of items stored as a variable", "words = ['this', 'that']"],
        'range': ["gives a range of numbers", "range(1,9)"],
        'index': ["access the position in a list, negatives wrap to the end, index() returns position", "words.index(0)"],
        'for': ["makes a for loop to iterate through list, related: while", "for word in words:"],
        'enumerate': ["tracks the index in a for loop", "for index, word in enumerate(words):"],
        'in': ['checks if a variable is in a list', "word in words"],
        'append': ['adds variable to end of list, related: insert, remove, del', "words.append('this')"],
        'remove': ['removes variable from list, related: insert, append, del', "words.remove('this')"],
        'insert': ['inserts variable to index of list, related: append, remove, del', "word.insert(0, 'this')"],
        'del': ['deletes at the index of list, related: insert, remove, append', "del words[1]"],
        'pop': ['remove variable from a list and store in new variable, default to end of list', 'word = words.pop(1)'],
        'sort': ['alphabetically sorts list, can reverse with argument reverse=True, related: sorted, reverse', 'words.sort()'],
        'sorted': ['temporarily alphabetically sorts list, can reverse with argument reverse=True, related: sort, reverse', 'sorted(words)'],
        'reverse': ['reverse order of list, related: sort, reverse', 'wrods.reverse()'],
        'len': ['returns the length of list', 'len(words)'],
        'slice': ['returns subset of a list starting at index and up to but not including next index', 'words[1:3]'],
        'min': ['returns minimum value of the list, related: max, sum', 'min(numbers)'],
        'max': ['returns maximum value of the list, related: min, sum', 'max(numbers)'],
        'sum': ['returns sum of all values of the list, related: max, min', 'sum(numbers)'],
        'comprehension': ['builds list from an operation', 'evens = [number*2 for number in range(1,11)]'],
        'find': ['returns index of a substring in a string, reverse with rfind()', "index_of_word = words.find('word')"],
        'replace': ['replaces substring with string', "new_string = old_string.replace('replace this', 'with that')"],
        'count': ['counts how many times substring appears in string', "number = string.count('this')"],
        'split': ['splits string into list of strings by providing a character', "words = message.split(' ')"],
        'tuple': ['a list that can not be modified', "tuple = ('this', that')"],
        'function': ['set of actions grouped together', "def function(arguement1, arguement2):",
        "can set default arguement with 'def fuction(arguement='default')",
        "can set arbitrary number of arguements with 'def function(*arguement):' or 'def function(**kwargs):' for keys"],
        'return': ['returns a value from a function, stops the function', 'return true'],
        'if': ['checks condition using ==, !=, <, >, <=, >=, in; returns True or False; elif, else can chain after', "if 'this' == 'that'"],
        'while': ['checks condition and starts loop if True, ends when it becomes False', "points = 0, while points < 5:"],
        'input': ['gets user input', "number = input('give me a number')"],
        'clear': ['clears screen, must import os', "os.system('cls')"],
        'sleep': ['waits some amount of time, must from time import sleep', "sleep(1)"],
        'pickle': ['saves a list as a file, import pickle', "file_object = open('animals.pydata', 'wb')...pickle.dump(animals, file_object)...file_object.close()"],
        'try': ['executes code, if any errors occur, runs the except line instead', "try:...except:..."],
        'dictionary': ['stores keys and values', "dictionary = {'key': 'value1', 'value2'}", "can add key-value or modify value with 'dictionary['key'] = 'value'",
        "can delete with 'del dictionary['key']", "can modify key with 'dictionary['new_key'] = dictionary['old_key']... del dictionary['old_key']",
        "can loop with 'for key, value in dictionary.items():'", "can loop keys with 'for key in dictionary'",
        "can loop values with 'for value in dictionary.values()'", "can loop in order with 'for word in sorted(dictionary):'"],
        'class': ['creats objects with sets of parameters and methods', "class Class(), def __init__(self): self.x = 0, def increase(self): self.x += 1"]

        }

def title_screen():
    print('----------------------------')
    print('-  PYTHON CODE DICTIONARY  -')
    print('----------------------------')

def wait():
    wait = input('\nhit enter to continue\n')

def show_words():
    os.system('cls')
    title_screen()
    all_words = ''
    line_count = 0
    for word in sorted(words.keys()):
        if line_count == 6:
            line_count = 0
            all_words = all_words + '\n'
        all_words = all_words + word
        if len(word) < 8:
            all_words = all_words + '\t\t'
        elif len(word) < 15:
            all_words = all_words + '\t'
        line_count = line_count + 1
    print(all_words)


def show_definition(query):
    os.system('cls')
    title_screen()
    print(query + '\n')
    for definition in words[query]:
        print(definition)
    print('\n----------------------------------------------------')
    wait()

os.system('cls')
quit = False
while quit == False:
    show_words()
    query = input("\nwhat word do you want to look up (or type 'q' to quit)?\n")
    if query == 'q':
        os.system('cls')
        print('quitting...')
        quit = True
    elif query in words.keys():
        show_definition(query)
    else:
        print("\nI don't know that word")
        wait()