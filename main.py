def main():
    book_path = "books/frankenstein.txt"
    file_text = get_book_text(book_path)
    split_text = file_text.split()
    word_count = count_words(split_text)
    char_freq = count_letters(split_text)
    

    print(f"--- Reporting output of {book_path} ---")
    print(f"{word_count} words found in the book\n")

    # Format and print character frequencies
    formatted_output = format_char(char_freq)
    print(formatted_output)

    print(f"--- End ---")

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()

def count_words(get_text):
    return len(get_text)

def count_letters(get_text):
    char_dict = {}
    for word in get_text:
        for char in word:
            lower_char = char.lower()
            if lower_char in char_dict:
                char_dict[lower_char] += 1
            else:
                char_dict[lower_char] = 1
    return char_dict

def format_char(char_freq):
    sorted_chars = sorted(char_freq.items(), key=lambda x: x[1], reverse=True)
    result = ""
    for char, freq in sorted_chars:
        if char.isalpha():
            result += f"The '{char}' character was found {freq} times\n"
    return result


main()
