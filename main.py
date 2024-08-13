def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count_result = word_count(text)
    character_count_result = count_characters(text)
    letter_count_result = count_letters(text)

    print(word_count_result) # word count
    print(character_count_result) # character count
    print(letter_count_result) #print the count of each letter in dictionary

def get_book_text(path):
    with open(path) as f:
        return f.read().lower() # convert the text to lowercase
# read book frankenstein
    
def word_count(text):
    words = text.split()
    count = len(words)
    return(count)
# count words function

def count_characters(text):
    return len(text)
# count characters function

def count_letters(text):
    letter_counts = {}
    for char in text:
        if char.isalpha():
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1
    return letter_counts
          
main()