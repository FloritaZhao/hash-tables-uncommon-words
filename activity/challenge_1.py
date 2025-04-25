from collections import Counter

def uncommon_from_sentences(sentences):
    word_list = []
    for sentence in sentences:
        word_list.extend([word for word in sentence.split()])
    word_counter = Counter(word_list)

    uncommon_word = [word for word, counter in word_counter.items() if counter ==1 ]

    return uncommon_word
