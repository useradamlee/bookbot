from stats import num_of_words, num_character, sort_dictionary
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit[1]
    character_count = num_character(sys.argv[1])
    sorted_dictionary = sort_dictionary(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_words(sys.argv[1])} total words")
    print("--------- Character Count -------")
    for dictionary in sorted_dictionary:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")
    print("============= END ===============")

main()
