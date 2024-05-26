words = ['hello', 'bye', 'yes', 'no', 'python',
         'apple', 'maybe', 'stepik', 'beegeek']

dct = {el: [ord(i) for i in el] for el in words}
print(dct)
