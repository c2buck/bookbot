def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count_result = word_count(text)
    character_count_result = count_characters(text)

    print(word_count_result)
    print(character_count_result)

def get_book_text(path):
    with open(path) as f:
        return f.read()
# read book frankenstein
    
def word_count(text):
    words = text.split()
    count = len(words)
    return(count)
# count words function

def count_characters(text):
    return len(text)
# count characters function
          
main()