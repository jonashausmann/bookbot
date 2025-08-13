
def get_books_text(path):
    with open(path) as f:
        return f.read()

def count_words(book_text):
    return len(book_text.split())

def count_letters(book_text):
    book_text.split()
    letter_count = {}
    for word in book_text:
        for letter in word:
            letter = letter.lower()
            if letter in letter_count:
                letter_count[letter] = letter_count[letter] + 1
            else:
                letter_count[letter] = 1


    return letter_count

def sort_on(items):
    return items["num"]

def double_dict(letter_count):
    double_list = []
    for letter in letter_count:
        double_dict = {}
        double_dict["char"] = letter
        double_dict["num"] = letter_count[letter]
        double_list.append(double_dict)

    double_list.sort(reverse=True, key=sort_on)
    return double_list







    















