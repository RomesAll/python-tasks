def reverse_words(sentence):
    list_sentence = sentence.split()
    return ' '.join(list_sentence[::-1])

sentence = 'the sky is blue'
result = reverse_words(sentence)
print(result)