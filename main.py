def pig_latin(*words, suffix="ay", single=False):
    list_words = []
    vowels = 'aeiou'

    for sentence in words:
        words_in_sentence = sentence.split()
        translated_sentence = []
    
        for word in words_in_sentence:
            
            
            if word[0].lower() in vowels:
                translated_word = word + suffix
            else:
                translated_word = word[1:] + word[0] + suffix
            translated_sentence.append((translated_word))
        
        if single:
            list_words.append(' '.join(translated_sentence))
        else:
            list_words.extend(translated_sentence)
    
    if single:
        return ' '.join(list_words)
    else:
        return list_words



#test case

test1_data = ["Word", "Apple"]
test1_config = {}

test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oy"}

test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}


result1 = pig_latin(*test1_data, **test1_config)
result2 = pig_latin(*test2_data, **test2_config)
result3 = pig_latin(*test3_data, **test3_config)

print(result1)
print(result2)
print(result3)