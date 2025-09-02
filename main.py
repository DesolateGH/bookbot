import sys
from stats import count_words, get_book_text, count_characters
def sort_on(items):
    return items["num"]
def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    num_words = count_words(book_path)

    print("----------- Word Count ----------")
    print(f'Found {num_words} total words')
    letters = count_characters(get_book_text(book_path));
    letters.sort(reverse=True, key=sort_on)

    print("--------- Character Count -------")
    for dictionary in letters:
        for key in dictionary:
            if key != "num":
                print(f'{key}: {dictionary['num']}')
    print("============= END ===============")
main()