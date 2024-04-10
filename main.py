# Combine two lists and remove duplicates in Python 

list1 = [1, 4, 6, 9]
list2 = [4, 6, 14, 7]

result = list1 + list(set(list2) - set(list1))
print(result)  # 👉️ [1, 4, 6, 9, 14, 7]
