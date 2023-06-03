def main():
    book_path = "books/frankenstein.txt"
    file_text = get_book_text(book_path)
    split_text = file_text.split()
    count_words(split_text)

def get_book_text(path):
    with open(path, "r") as f:
        return f.read()
    
def count_words(book_content):
    counter = 0
    for word in book_content:
        counter += 1
    print(counter)
        
    
    
main()
