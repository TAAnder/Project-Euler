
max_totient_ratio = 1
best_n = 1

# 831600

# for n in range(2,20):
#     i=2
#     tot = n
#     t_ratio = i/tot
#     while i<n and t_ratio > max_totient_ratio:
#         if n%i != 0:
#             tot-=1
#         t_ratio = i/tot
#         i +=1
#     if t_ratio > max_totient_ratio:
#         best_n = n
#         max_totient_ratio = t_ratio
#         print(f'{n=} and {t_ratio= }')
#     if n < max_totient_ratio:
#         break