def main():
    book_path = "github.com/OsSiCl/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    print(text)
    print(word_count)
    print(character_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(full_text):
    words = full_text.split()
    return len(words)

def count_characters(full_text):
    dict_count={}

    for item in full_text:
        char = str(item).lower()

        if char not in dict_count:
            dict_count[char] = 1
        else:
            dict_count[char] += 1
    return dict_count
    
main()