class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine = magazine

    @property
    def author(self):
        return self._author
    @author.setter
    def author(self,author):
        if isinstance(author,Author):
            self._author = author
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if not hasattr(self,"_title") and isinstance(title,str) and 5<=len(title)<=50:
            self._title = title
    def __repr__(self):
        return f"{self.author} {self.magazine} {self.title}"   
class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,new_name):
        if not hasattr(self,"_name") and isinstance(new_name,str)and  len(new_name):
            self._name = new_name

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        topics = list({magazine.category for magazine in self.magazines()})
        return topics if topics else None
    def __repr__(self):
        return f"{self.name}"
class Magazine:
    all=[]
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)
    
    @property 
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        if isinstance(name,str)and 2<=len(name)<=16:
            self._name = name

    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category):
            self._category = category

    def articles(self):
        return[article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({magazine.author for magazine in self.articles()})

    def article_titles(self):
        titles = [magazine.title for magazine in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        authors = [magazine.author for magazine in self.articles()]
  
        return authors if len(authors) > 2 else None
    def __repr__(self):
        return f"{self.name} {self.category}"
    @classmethod
    def top_publisher(cls):
        # Check if there are any magazines in the list
        if not cls.all:
            return None

        # Find the magazine with the most articles
        return max(cls.all, key=lambda magazine: len(magazine.articles()), default=None)
        # print(top_magazine)
        # # Return the magazine with the most articles
        # return top_magazine if len(top_magazine.articles())  else None
author1 = Author("Alex")
author2 = Author("Jack")
magazine1 = Magazine("Beyong Universe","Astro")
magazine2 = Magazine("Green Air","Nature")

author1.add_article(magazine1,"Dark Sky")
author1.add_article(magazine2,"Fresh it!")
author2.add_article(magazine1,"Dark sky")

print(author2.magazines())