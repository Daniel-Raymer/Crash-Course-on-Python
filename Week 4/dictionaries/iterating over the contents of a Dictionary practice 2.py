def count_letters(text):
    result = {}
    for i in text:
        if i not in result:
            result[i] = 0
        result[i] += 1
    return result

count_letters("tenant")