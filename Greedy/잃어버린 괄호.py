# import sys

# S = sys.stdin.readline()

# idx = [0]

# result = eval(S)

# for i, s in enumerate(S):
#     if(s == '+' or s == '-'):
#         idx.append(i)

# idx.append(int(len(S) - 1))

# print(idx)

# for i in range(len(idx) - 1):
#     for j in range(i + 1, len(idx)):
#         tmpS = S
#         first = idx[i]
#         second = idx[j]
#         if first == 0:
#             tmpS = '(' + tmpS
#         else:
#             tmpS = tmpS[:first + 1] + '(' + tmpS[first + 1:]

#         if second != (int(len(S) - 1)):
#             tmpS = tmpS[:second + 1] + ')' + tmpS[second + 1:]
#         else:
#             tmpS = tmpS + ')'
#         print(tmpS)

import sys

S = sys.stdin.readline()
tmps = S
tmps = tmps.replace('+', '-').replace('\n','')

slist = tmps.split('-')

print(slist)