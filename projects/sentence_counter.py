sentence = input("Give us a sentence:")

char_sentence_list = list(sentence)

lowercase = 'qwertyuiopasdfghjklzxcvbnm'
uppercase = 'QWERTYUIOPASDFGHJKLZXCVBNM'
punctuation = '!@#$%^&*()_-,./;\'\"\\'

l_list = list(lowercase)
u_list = list(uppercase)
p_list = list(punctuation)

results = {
    "lower": 0,
    "upper": 0,
    "punct": 0,
    "total": 0
}



for ch in char_sentence_list:
    if ch in l_list:
        results["lower"] +=1
        results["total"] +=1
    elif ch in u_list:
        results["upper"] +=1
        results["total"] +=1
    elif ch in p_list:
        results["punct"] +=1
        results["total"] +=1

print(f'Lower: {results["lower"]} \nUpper: {results["upper"]} \nPunctuation: {results["punct"]} \nTotal: {results["total"]} ')