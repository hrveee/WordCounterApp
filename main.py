def open_file_and_convert_them_into_list(filename):
  """ Open and read text file, then convert them to paragraph"""

  # defining paragraph_list as an empty list
  paragraph_list = []

  # opening the file, then append each paragraph to the   paragraph_list
  with open(filename, 'r') as textFile:
    text_data = textFile.readlines()

    # append each paragraph to the paragraph_list
    for item in text_data:
      item.strip()
      if len(item) > 1:
        paragraph_list.append(item.replace("\n", ""))
      else:
        continue

  # return the paragraph_list
  return paragraph_list


def count_words(filename):
  """ Count how many words that text file have. """

  # creating paragraph_list variable to store each paragraphs
  paragraph_list = open_file_and_convert_them_into_list(filename)

  # defining count_words as 0 use for the loop
  count_words = 0

  # defining words_list as empty list
  words_list = []

  # append each words in paragraph_list to words_list
  for words in paragraph_list:
    words_list.append(words.split(" "))
  # count each words in words_list using method of nesting loop
  for paragraphs in words_list:
    for words in paragraphs:
      count_words += 1

  # return the count_words
  return count_words


def main():

  # prompt user to input their text file name
  filename = input("Enter the name of the text file (with the extension): ")

  # defining total_count_words to save result of count_words function 
  total_count_words = count_words(filename)

  # print total of count words
  print("\nTotal of words in this text file is {} words".format(total_count_words))


if __name__ == '__main__':
  main()
