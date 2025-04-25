from collections import Counter

def uncommon_from_sentences(s1, s2):
    word_list = [word for word in s1.split()] + [word for word in s2.split()]
    word_counter = Counter(word_list)

    uncommon_word = [word for word, counter in word_counter.items() if counter ==1 ]

    return uncommon_word
