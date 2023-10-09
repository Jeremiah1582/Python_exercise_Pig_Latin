
def pig_latin(*args, suffix='ay', single=False):
    # print(*args, suffix, single)
    vowels = 'aeiou'
    results =[]
        
    for phrase in args:
      for word in phrase.split(' '):
        # print(word)
        if word[0].lower() in vowels:
            new_word=word+suffix
            results.append(new_word)
        else: 
            new_word = word[1:]+word[0]+suffix
            results.append(new_word)
    if single: 
        return(' '.join(results))
    return(results)
        
        
        
# Test cases
test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions",]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(*test1_data, **test1_config))
print(pig_latin(*test2_data, **test2_config))
print(pig_latin(*test3_data, **test3_config))