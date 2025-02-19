class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    # Title Validation
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if isinstance(title,str) and not hasattr(self,"_title") and 5 <= len(title)<= 50:
            self._title = title

    # Author validation
    @property
    def author(self):
        return self._author
    @author.setter
    def  author(self,author):
        if isinstance(author,Author):
            self._author = author
    
    # Magagine validation
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine(self,magazine):
        if isinstance(magazine,Magazine):
            self._magazine = magazine
class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,name):
        if isinstance(name,str) and not hasattr(self,"_name") and len(name):
            self._name = name


    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        topics =  list({magazine.category for magazine in self.magazines()})
        return topics if topics else None

class Magazine:
    all = []
    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # Name Validation 
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self,name):
        if isinstance(name,str) and 2 <= len(name) <= 16:
            self._name = name

    # Category validation
    @property
    def category(self):
        return self._category
    @category.setter
    def category(self,category):
        if isinstance(category,str) and len(category):
            self._category = category

    def articles(self):
        return [ article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({magazine.author for magazine in self.articles()})

    def article_titles(self):
        artticles = [article.title for article in self.articles()]
        return artticles if artticles else None

    def contributing_authors(self):
        authors = [magazine.author for magazine in self.articles()]
        return authors if len(authors) > 2 else None 
    @classmethod
    def top_publisher(cls):
        return max(cls.all, key=lambda magazine:len(magazine.articles()),default=None)