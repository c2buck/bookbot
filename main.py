def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    word_count_result = word_count(text)
    character_count_result = count_characters(text)
    letter_count_result = count_letters(text)

    print(f"Total word count: {word_count_result}") #word count
    print(f"Total character count: {character_count_result}") #character count

    #convert the dictionary to a list of dictionaries
    letter_count_list = [{"char": char, "count": count} for char, count in letter_count_result.items()]

    #sort the list of dictionaries by the "count" value             
    letter_count_list.sort(key=lambda x: x["char"])

    for item in letter_count_list:
        print(f"The '{item['char']}' character was found {item['count']} times")

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