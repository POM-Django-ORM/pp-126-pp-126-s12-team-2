from django.db import models
from author.models import Author


class Book(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True) 
    count = models.IntegerField(default=10)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return f"'id': {self.id}, 'name': '{self.name}', 'description': '{self.description}', 'count': {self.count}, 'authors': {[author.id for author in self.authors.all()]}"



    def __repr__(self):
        return f'Book(id={self.id})'

    @staticmethod
    def get_by_id(book_id):
        try:
            return Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return None

    @staticmethod
    def delete_by_id(book_id):
        book = Book.get_by_id(book_id)
        if book:
            book.delete()
            return True
        return False

    @staticmethod
    def create(name, description, count=10, authors=None):
        book = Book.objects.create(name=name, description=description, count=count)
        if authors:
            book.authors.set(authors)
        return book

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'count': self.count,
            'authors': [author.name for author in self.authors.all()]
        }

    def update(self, name=None, description=None, count=None):
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if count is not None:
            self.count = count
        self.save()

    def add_authors(self, authors):
        self.authors.add(*authors)

    def remove_authors(self, authors):
        self.authors.remove(*authors)

    @staticmethod
    def get_all():
        return list(Book.objects.all().order_by('id'))

