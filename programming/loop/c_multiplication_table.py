# for i in range(1,11):
#     for j in range(1,11):

#         # print(i*j)
#         print(i, '*', j, '=', i*j)
#     print('\t')

n = int(input("Enter any number:"))
for n in range(1,n+1):
    for j in range(1,11):
        print(f'{n} x {j} = {n*j}')