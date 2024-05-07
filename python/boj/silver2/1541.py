# from sys import stdin
# input = stdin.readline

# exp = input().strip()
# result = 0
# isCalcMinus = False
# start = 0
# # 48 ~ 57

# for idx,ch in enumerate(exp):
#     if ch == '+' or ch == '-':
#         num = int(exp[start:idx])
#         start = idx + 1 # 숫자 만들기
        
#         if isCalcMinus:
#             result -= num
#         else:
#             result += num
#         if ch == '-':
#             isCalcMinus = True

# last_number = int(exp[start:])
# if isCalcMinus:
#     result -= last_number
# else:
#     result += last_number
# print(result)

print(eval('1+2+3-3'))