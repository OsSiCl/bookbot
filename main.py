def main():
    book_path = "github.com/OsSiCl/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    print(text)
    print(word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(full_text):
    words = full_text.split()
    return len(words)
    
main()