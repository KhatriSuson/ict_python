def count_vowels(str):
    v = 'aeiouAEIOU'
    count = 0
    
    for char in str:
        if char in v:
            count += 1
            
    return count

print(count_vowels('applebanana'))