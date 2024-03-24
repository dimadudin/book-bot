def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_num = get_word_num(text)
    char_dict = get_char_dict(text)
    char_list = char_dict_to_list(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{word_num} words found in the document")
    print()

    for item in char_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_word_num(text):
    words = text.split()
    return len(words)


def sort_on(d):
    return d["num"]


def char_dict_to_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list


def get_char_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
