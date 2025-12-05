#عمر وليد شعبان عبدالخالق (IS) sec(2)
#Q1
products = ["  LAPTOP ", "phone  ", "  Tablet", "CAMERA  "]
cleaned = list(map(lambda s: s.strip().title(), products))
print(cleaned)
#//////////////////OUTPUT///////////////////////
# Output: ['Laptop', 'Phone', 'Tablet', 'Camera']
#--------------------------------------------------------
#Q2
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (9/5)*c + 32, celsius))
print(fahrenheit)
#//////////////////OUTPUT///////////////////////
# Output: [32.0, 50.0, 68.0, 86.0, 104.0]
#-----------------------------------------------------
#Q3
nums = [1, 2, 3, 4, 5]
result = list(map(lambda x: x**2 + 10, nums))
print(result)
#//////////////////OUTPUT///////////////////////
# Output: [11, 14, 19, 26, 35]
#--------------------------------------------------------
#Q4
words = ["python", "lambda", "programming", "map", "function"]
pairs = list(map(lambda w: (w[0], w[-1]), words))
print(pairs)
#//////////////////OUTPUT///////////////////////
# Output: [('p', 'n'), ('l', 'a'), ('p', 'g'), ('m', 'p'), ('f', 'n')]
#--------------------------------------------------------
#Q5
marks = [[45, 80, 70], [90, 60, 100], [88, 76, 92]]
updated = list(map(lambda row: list(map(lambda x: round(x * 1.05), row)), marks))
print(updated)
#//////////////////OUTPUT///////////////////////
# Output: [[47, 84, 74], [95, 63, 105], [92, 80, 97]]
#--------------------------------------------------------
#Q6
nums = [10, 20, 30, 40, 50]

mn, mx = min(nums), max(nums)
normalized = [0.0]*len(nums) if mn == mx else [(x-mn)/(mx-mn) for x in nums]
print(normalized)
#//////////////////OUTPUT///////////////////////
# Output: [0.0, 0.25, 0.5, 0.75, 1.0]
#--------------------------------------------------------
#Q7 sentences = [
sentences = [ "hello world","this is a test","map and lambda are useful"]
result = [ [len(w) for w in s.split()] for s in sentences ]
print(result)
#//////////////////OUTPUT///////////////////////
#[[5, 5], [4, 2, 1, 4], [3, 3, 6, 3, 6]]








