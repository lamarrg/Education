
#text = "This is my test text. We're keeping this text short to keep things manageable."

def count_words(text):
    """
    Count the number of times each word occurs in text (str). Return ditiontary where keys are unique words and values are word counts. Skip punctuation
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts


from collections import Counter

def count_words_fast(text):
    """
    Count the number of times each word occurs in text (str). Return ditiontary where keys are unique words and values are word counts. Skip punctuation
    """
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"']
    for ch in skips:
        text = text.replace(ch, "")

    word_counts = Counter(text.split(" "))
    return word_counts

def read_book(title_path):
    """
    This function will read a book and return it as a string.
    """
    with open(title_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text

def word_stats(word_counts):
    num_unique = len(word_counts)
    num_unique = int(num_unique)
    counts = word_counts.values()
    return (num_unique, counts)


#print(count_words_fast(text))
text = read_book("Romeo and Juliet.txt")

word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)

#print(num_unique)   # this line prints out 7134

# print(len(text))
# print(text.find("What's in a name?"))
# print(text[49383:50383])