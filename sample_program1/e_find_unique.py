from collections import Counter

def unique(lst):
    counts = Counter(lst)
    
    unique = [item for item, count in counts.items() if count ==1]
    return unique
    