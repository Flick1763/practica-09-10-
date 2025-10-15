def preprocess_pattern(pattern):
    bad_char = {}
    for index, char in enumerate(pattern):
        bad_char[char] = index
    return bad_char

def boyer_moore(text, pattern):
    bad_char = preprocess_pattern(pattern)
    m = len(pattern)
    n = len(text)
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            print(f'Pattern found at index {s}')
            s += (m - bad_char.get(text[s + m], -1)) if s + m < n else 1
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))

text = "ABABDABACDABABCABAB"
pattern = "ABABC"
boyer_moore(text, pattern)
print("Работу выполнил Брагин Артём")
#Пояснение
#preprocess_pattern создает таблицу неудачного символа для улучшения поиска.
#boyer_moore реализует сам алгоритм поиска подстроки, используя эту таблицу.
#Алгоритм эффективен, поскольку он избегает ненужного сравнения символов.