from stats import count_words
from stats import get_books_text
from stats import count_letters
import stats
import sys

def main():
    input_list = sys.argv
    if len(input_list) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = input_list[1]

    text = get_books_text(book_path)
    num_words = count_words(text)

    print("============ BOOKBOT ============")
    print("Analyzing book found at ")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    letter_count = count_letters(text)
    double_list = stats.double_dict(letter_count)
    for dict_value in double_list:
        if dict_value["char"].isalpha():
            print(f"{dict_value["char"]}: {dict_value["num"]}")

    print("============= END ===============")
main()



