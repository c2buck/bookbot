def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count_result = word_count(text)
    character_count_result = count_characters(text)
    letter_count_result = count_letters(text)

    print(f"--- Begin report of {book_path} ---")
    print(f"Total word count: {word_count_result}") #word count
    
    #convert the dictionary to a list of dictionaries
    letter_count_list = [
        {"char": char, "count": count} for char, count in letter_count_result.items()
        ]

    #sort the list of dictionaries by the "count" value             
    letter_count_list.sort(key=sort_on)

    for item in letter_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

def sort_on(dict):
    return dict["char"]

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
    letter_counts = {}  # Create an empty dictionary to store the count of each letter
    for char in text:  # Iterate over each character in the text
        if char.isalpha():  # Check if the character is a letter (ignores numbers, punctuation, etc.)
            if char in letter_counts:  # If the letter is already in the dictionary, increment its count
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1  # If the letter is not in the dictionary, add it with a count of 1
    return letter_counts  # Return the dictionary containing the counts of each letter
        
main()

print("--- End report ---")