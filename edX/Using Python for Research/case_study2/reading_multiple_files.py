import os
import pandas as pd
import language_processing as lang

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

print(stats.head())