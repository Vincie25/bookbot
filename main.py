import sys
from stats import numwords, numchar, dic_list


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
    return file_content


def main():
    try:
        file = sys.argv[1]
    except IndexError:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    content = get_book_text(file)
    number = numwords(content)
    total_chars = numchar(content)
    sor_ch = dic_list(total_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file}")
    print("----------- Word Count ----------")
    print(f"Found {number} total words")
    print("--------- Character Count -------")
    for i in sor_ch:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")



if __name__ == '__main__':
    main()
