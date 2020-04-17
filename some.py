def h(k):
    return (7*k + 3) % 13

nums = [31, 45, 14, 89, 24, 95, 12, 38, 27, 16, 25] 
for num in nums:
    print( h(num), num)