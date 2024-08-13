def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = word_count(text)
    print(count)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def word_count(text):
    words = text.split()
    count = len(words)
    return(count)

def count_characters(text):
    count_characters = count_characters(text)
    print(count_characters)
    return len(text)
           
main()