# s = "dsnvfnvoinfiondiceirwnvdhfuirbunviureib"

# charSet = set()
# res = 0
# l = 0

# for r in range(len(s)):
#     while s[r] in charSet:
#         charSet.remove(s[l])
#         print(charSet)
#         l += 1
#     charSet.add(s[r])
#     print(charSet)
#     res = max(res, r - l + 1)
# print(res)
# s = "ABCBABC"
# count = {}
# for r in range(len(s)):
#     count[s[r]] = 1 + count.get(s[r], 0)
#     print(count[s[r]])
# print(max(count.values()))
# def bubble():
#     s = [1,5,3,6,8,3,4,6,7,3,6,7,9,5]
#     # print(s)
#     for i in range(len(s)):
        
#         for j in range(len(s) - i - 1):
#             print(len(s) - i - 1,end = "")
#             if s[j] > s[j + 1]:
#                 s[j], s[j + 1] = s[j + 1], s[j]
    
#     # print(s)
    
# bubble()

# s, t = "ADOBECODEBANC", "ABC"


# countT, window = {}, {}

# for c in t:
#     countT[c] = 1 + countT.get(c, 0)
    
# have, need = 0, len(countT)
# l = 0
# res, resLen = [-10, 0], float("infinity")
# for r in range(len(s)):
#     window[s[r]] = 1 + window.get(s[r], 0)
    
#     if s[r] in countT and window[s[r]] == countT[s[r]]:
#         have += 1
#     while have == need:
#         if (r - l + 1) < resLen:
#             res = [l, r]
#             resLen = r - l + 1
#         window[s[l]] -= 1
#         if s[l] in countT and window[s[l]] < countT[s[l]]:
#             have -= 1
#         l += 1
# l, r = res
# print(s[l:r + 1] if resLen != float("infinity") else "")

# s = "{[()}]"
# stack = []
# maps = {')':'(', ']':'[', '}':'{'}


# for c in s:
#     if c in maps:
#         if stack[-1] == maps[c]:
#             stack.pop()

#         else:
#             False
#     else:
#         stack.append(c)
#     print(stack)
# print(True if not stack else False)

# position = [10,8,0,5,3] 
# speed = [2,4,1,1,3]
# pair = [[p, s] for p, s in zip(position, speed)]

# pair.sort()
# print(pair[::-1]) 
