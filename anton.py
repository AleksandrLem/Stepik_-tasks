# n = int(input('n='))
# lst = [input('str=') for _ in range(n)]
# num = []

# for strk in range(len(lst)):
#     s = ''
#     for i in 'anton':
#         if i in lst[strk]:
#             s+=i
#     if s == 'anton':
#         num.append(strk+1)
# print(*num)

def filter_anton(str_lst):
    return str_lst in 'anton'


s1 = filter(filter_anton, '222anton456')
s2 = filter(filter_anton, 'a1n1t1o1n1')
s3 = filter(filter_anton, '0000a0000n00t00000o000000n')
s4 = filter(filter_anton, 'gylfole')
s5 = filter(filter_anton, 'richard')
s6 = filter(filter_anton, 'ant0n')
s7 = filter(filter_anton, '6')
s8 = filter(filter_anton,
            'osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen')


print(*s8)
