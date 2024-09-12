def anagram_check(str1, str2):
    
    return sorted(str1) == sorted(str2)


print(anagram_check("listen", "silent"))
print(anagram_check('world', 'nepal'))