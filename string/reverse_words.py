# Python's string is immutable, so the string will have to be converted
# into character array
def reverse_words(sentence):
    sentence_rev = List(sentence[:])
    n = len(sentence)
    if n < 2:
        return "".join(sentence_rev)
    reverse_substring(sentence_rev, 0, n-1)
    i = 0
    while i < n:
        while sentence_rev[i] == " " and i < n:
            i += 1
        if i == n:
            break
        start = i + 1
        i += 1
        while i < n and sentence_rev[i] != " ":
            i += 1
        end = i - 1
        reverse_substring(sentence_rev, start, end)
    return "".join(sentence_rev)

def reverse_substring(sentence, start, end):
    if start == end || end - start == 1:
        return sentence
    mid = (start + end)/2
    i = start
    j = end
    while i <= mid:
        sentence[i], sentence[j] = sentence[j], sentence[i]
        i += 1
        j -= 1
