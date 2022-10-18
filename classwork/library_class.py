# You have a Library which have an Articles and each Article have It's author.
# Make it possible for Library class - to print all authors with a list of their articles.

class Author:
    def __init__(self, name):
        self.name = name


class Article:
    def __init__(self, name: str, author: Author):
        self.name = name
        self.author = author


class Library:
    def __init__(self, name, articles):
        self.name = name
        self.articles = articles

    def get_author_with_his_articles(self):  # return {"john": [article_1, article_2]}
        temp_dict = {}
        for article in self.articles:
            if article.author.name not in temp_dict:
                temp_dict[article.author.name] = [article]
            else:
                temp_dict[article.author.name].append(article)
        return temp_dict


# new_author = Author("Oana")
# my_article = Article("my_article", new_author)
# my_lib = Library("Huge", my_article)
# print(my_lib.get_author_with_his_articles())

author_1 = Author('John')

article_1 = Article("article_1", author_1)
article_2 = Article("article_2", author_1)

library = Library('lib_1', [article_1, article_2])

print(library.get_author_with_his_articles())
assert library.get_author_with_his_articles() == {"John": [article_1, article_2]}
