def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    letters = {}
    fmt_text = text.lower()
    for ch in fmt_text:
        if ch.isalpha():
            if ch in letters:
                letters[ch] += 1
            else:
                letters[ch] = 1
    return list(letters.items())


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(count_words(file_contents))

        letters = count_letters(file_contents)
        letters.sort()
        for letter, num in letters:
            print(f"The '{letter}' character was found {num} times")


main()
