word_list = []
stop_word_list = []
final_word_list = []
with open('neuromancer.txt', 'r') as f:
    for line in f:
        for word in line.split():
            word = word.lower()
            word_list.append(word)
with open('stop_words.txt', 'r') as f:
    for line in f:
        for word in line.split(","):
            stop_word_list.append(word)


for word in word_list:
    if word not in stop_word_list :
        final_word_list.append(word)


print(final_word_list)

  