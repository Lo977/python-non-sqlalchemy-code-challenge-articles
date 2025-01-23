class Article:
    all =[]
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if not hasattr(self,"_title") and isinstance(title,str) and 5 <= len(title) <= 50:
            self._title = title
        # else:
        #     raise ValueError("Titile Error")
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author  

    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine = magazine

            
class Author:
    all =[]
    def __init__(self, name):
        self.name = name
        Author.all.append(self)

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if not hasattr(self,"_name") and len(name) > 0 and isinstance(name,str):
            self._name = name 
        # else:
        #     raise ValueError("Can not change")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        magazine_topic = list({magazine.category for magazine in self.magazines()})
        return magazine_topic if magazine_topic else None

class Magazine:
    all =[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category) > 0:
            self._category = category


    def articles(self):
        return [article for article in Article.all if article.magazine == self ]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        titles = [magazine.title for magazine in self.articles()]   
        return titles if titles else None

    def contributing_authors(self):
        authors = [magazine.author for magazine in self.articles()]
        return authors if len(authors) > 2 else None