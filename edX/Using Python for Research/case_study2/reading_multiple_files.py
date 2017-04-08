import os
import pandas as pd
import language_processing as lang
import matplotlib.pyplot as plt

# This file reads in multiple books in a directory, reads in the total amount of words, the amount of unique words, puts them in a panda table and charts them. 

stats = pd.DataFrame(columns = ("language", "author", "title", "length", "unique"))

book_dir = "./books"
title_num = 1
for language in os.listdir(book_dir):
    if not language.startswith("."):
        for author in os.listdir(book_dir + "/" + language):
            if not author.startswith("."):
                for title in os.listdir(book_dir + "/" + language + "/" + author):
                    if not title.startswith("."):
                        inputfile = book_dir + "/" + language + "/" + author + "/" + title
                        print(inputfile)
                        text = lang.read_book(inputfile)
                        (num_unique, counts) = lang.word_stats(lang.count_words(text))
                        stats.loc[title_num] = language, author.capitalize(), title[:-4], sum(counts), num_unique
                        title_num += 1

#print(stats.head())

#print(stats.unique)

#plt.plot(stats.length, stats.unique, "bo")

# plt.loglog(stats.length, stats.unique, "bo")
# plt.show()

print(stats[stats.language == "german"])

plt.figure(figsize= (10,10))
subset = stats[stats.language == "english"]
plt.loglog(subset.length, subset.unique, "o", label = "english", color = "crimson")

subset = stats[stats.language == "german"]
plt.loglog(subset.length, subset.unique, "o", label = "german", color = "forestgreen")

subset = stats[stats.language == "spanish"]
plt.loglog(subset.length, subset.unique, "o", label = "spanish", color = "orange")

plt.legend()
plt.xlabel("Book Length")
plt.ylabel("Number of unique words")
plt.savefig("lang_plot.pdf")

print(stats.length)
print(stats["length"])