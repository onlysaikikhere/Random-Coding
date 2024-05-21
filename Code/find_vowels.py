import re
def get_count(sentence):
    vowels = r'[aeiouAEIOU]'
    count = len(re.findall(vowels, sentence))
    return(count)