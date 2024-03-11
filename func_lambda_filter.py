words = ['beverage', 'monday', 'abroad', 'bias', 'abuse',
         'abolish', 'abuse', 'abuse', 'bid', 'wednesday',
         'able', 'betray', 'accident', 'abduct', 'bigot',
         'bet', 'abandon', 'besides', 'access', 'friday',
         'bestow', 'abound', 'absent', 'beware', 'abundant',
         'abnormal', 'aboard', 'about', 'accelerate', 'abort',
         'thursday', 'tuesday', 'sunday', 'berth', 'beyond',
         'benevolent', 'abate', 'abide', 'bicycle', 'beside',
         'accept', 'berry', 'bewilder', 'abrupt', 'saturday',
         'accessory', 'absorb']

# слова из списка words, имеющие длину ровно 6 символов в алфавитном порядке
words_len = sorted(filter(lambda word: len(word) == 6, words))
print(*list(words_len))
