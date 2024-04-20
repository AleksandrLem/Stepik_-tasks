s1 = 'Awful Terrible'.split()
s2 = 'Beautiful Pretty'.split()
s3 = 'Great Excellent'.split()
s4 = 'Generous Bountiful'.split()

lst = [s1, s2, s3, s4]
d = {}
d[s1[0]]=s1[1]



# создаем словарь, где сначала первое слово - ключ, второе значение,
# затем второе - ключ, первое - значение

for i in lst:
    d[i[0]]=i[1]
for i in lst:
    d[i[1]]=i[0]

print(d.get('Excellent', 'такого слова нет'))

# Решение, которое намного проще
# words = {}
# for _ in range(int(input())):
#     a, b = input().split()
#     words[a], words[b] = b, a
# print(words[input()])
