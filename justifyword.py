def maximize_words(k, words, n, m):
    valid_words = [word for word in words if len(word) <= m]
    if not valid_words:
        return 0

    total_words = 0
    line_used = 0
    line_space = 0

    for word in valid_words:
        required_space = len(word) if line_space == 0 else len(word) + 1
        if line_space + required_space <= m:
            line_space += required_space
            total_words += 1
        else:
            line_used += 1
            if line_used >= n:
                break
            line_space = len(word)
            total_words += 1

    return total_words

k = int(input().strip())
words = [input().strip() for _ in range(k)]
n, m = map(int, input().strip().split())
print(maximize_words(k, words, n, m))
