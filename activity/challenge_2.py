def uncommon_from_sentences(sentences):
#     - Challenge #2
#   - Allow a word to appear any number of times in a single sentence for it to still be considered uncommon. If it appears in more than one sentence, then it is no longer uncommon.
    result = []
# 先把每一个sentence里面的Set给弄出来，然后再减其他的Set
    for i, sentence in enumerate(sentences):
        word_i_set = set(sentence.split())
    
        other_words_set = set()
    
        for j, sentence in enumerate(sentences):
            if i == j:
                continue
            other_words_set |= set(sentence.split())
    
        uncommon = word_i_set - other_words_set
        result.extend(uncommon)
    
    return result
