import sys, os
from stats import word_count, letter_count, sort_dict

def get_book_text(file_path):
  with open(file_path) as f:
    return f.read()

def print_report(book_path):
  book_text = get_book_text(book_path)
  num_words = word_count(book_text)
  num_letters = letter_count(book_text)
  letter_list = sort_dict(num_letters)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {book_path}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  for letter in letter_list:
    print(f"{letter["char"]}: {letter["num"]}")
  print("============= END ===============")

def main():
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

  book_path = sys.argv[1]
  if not os.path.exists(book_path):
    print(f"Book file not found at {book_path}")
    sys.exit(1)

  print_report(book_path)

main()