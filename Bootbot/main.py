from stats import count_words, count_char, sort_on
import sys
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents



def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    sort_list = []
    total_words = count_words(sys.argv[1])
    
    char = count_char(sys.argv[1])

    print("Usage: python3 main.py <path_to_book>")
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at " + sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {total_words} total words")
    print("--------- Character Count -------")

    for car, count in char.items():
        pair = {"char": car, "num": count}
        sort_list.append(pair)
    sort_list.sort(reverse=True, key=sort_on)
    
    for item in sort_list:
        ch = item["char"]
        numb = item["num"]
        if ch.isalpha():
            print(f"{ch}: {numb}")

main()