def parse_3x3_matrix(matrix, n):
    char_map = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"],
        '+': ["   ", " _ ", " | "],
        '-': ["   ", " _ ", "   "],
        '*': ["   ", " | ", " | "],
        '%': [" | ", "   ", " | "],
        '=': ["   ", " _ ", " _ "]
    }
    inverse_char_map = {tuple(v): k for k, v in char_map.items()}
    chars = []

    for i in range(n):
        char = tuple(row[i * 3:(i + 1) * 3] for row in matrix)
        if char in inverse_char_map:
            chars.append(inverse_char_map[char])
        else:
            chars.append(None)

    return chars


def evaluate_equation(chars):
    result = int(chars[0])
    i = 1
    while i < len(chars) - 2:
        operator = chars[i]
        operand = int(chars[i + 1])
        if operator == '+':
            result += operand
        elif operator == '-':
            result -= operand
        elif operator == '*':
            result *= operand
        elif operator == '%':
            result %= operand
        i += 2

    return result


def find_faulty_character(n, matrix):
    char_map = {
        '0': [" _ ", "| |", "|_|"],
        '1': ["   ", "  |", "  |"],
        '2': [" _ ", " _|", "|_ "],
        '3': [" _ ", " _|", " _|"],
        '4': ["   ", "|_|", "  |"],
        '5': [" _ ", "|_ ", " _|"],
        '6': [" _ ", "|_ ", "|_|"],
        '7': [" _ ", "  |", "  |"],
        '8': [" _ ", "|_|", "|_|"],
        '9': [" _ ", "|_|", " _|"],
        '+': ["   ", " _ ", " | "],
        '-': ["   ", " _ ", "   "],
        '*': ["   ", " | ", " | "],
        '%': [" | ", "   ", " | "],
        '=': ["   ", " _ ", " _ "]
    }

    inverse_char_map = {tuple(v): k for k, v in char_map.items()}
    chars = parse_3x3_matrix(matrix, n)
    rhs = int(chars[-1])
    lhs_chars = chars[:-2]

    for i, original_char in enumerate(lhs_chars):
        original_pattern = char_map[original_char]
        for toggle_row in range(3):
            for toggle_col in range(3):
                new_pattern = [list(row) for row in original_pattern]
                new_pattern[toggle_row][toggle_col] = ' ' if original_pattern[toggle_row][toggle_col] == '_' else '_'
                new_pattern = tuple(''.join(row) for row in new_pattern)
                if new_pattern in inverse_char_map:
                    chars[i] = inverse_char_map[new_pattern]
                    if evaluate_equation(chars[:-2]) == rhs:
                        return i + 1
                chars[i] = original_char

    return -1


n = int(input())
matrix = [input() for _ in range(3)]
print(find_faulty_character(n, matrix))
