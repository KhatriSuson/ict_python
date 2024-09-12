from collections import Counter

def unique(lst):
    counts = Counter(lst)
    
    unique = [item for item, count in counts.items() if count ==1]
    return unique
    
    
numbers = [1,2,2,3,4,4]
result = unique(numbers)
print(result)