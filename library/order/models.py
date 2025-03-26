from django.db import models
from django.utils import timezone
from authentication.models import CustomUser
from book.models import Book
import time


class Order(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(null=True)
    end_at = models.DateTimeField(null=True)
    plated_end_at = models.DateTimeField(null=True)


    def __str__(self):
        return f"{self.id}, {self.user.id}, {self.book.id}, {self.created_at}, {self.end_at}, {self.plated_end_at}"

    def __repr__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.id,
            'book': self.book.id,
            'created_at': self.created_at,
            'end_at': self.end_at,
            'plated_end_at': self.plated_end_at,
        }

    @staticmethod
    def create(user, book, plated_end_at):
        now = timezone.now()
        order = Order(user=user, book=book, created_at=now, plated_end_at=plated_end_at)
        order.save()
        return order

    @staticmethod
    def get_by_id(order_id):
        return Order.objects.filter(id=order_id).first()

    def update(self, plated_end_at=None, end_at=None):
        if plated_end_at is not None:
            self.plated_end_at = plated_end_at
        if end_at is not None:
            self.end_at = end_at
        self.save()

    @staticmethod
    def get_all():
        return Order.objects.all()

    @staticmethod
    def get_not_returned_books():
        return Order.objects.filter(end_at__isnull=True)

    @staticmethod
    def delete_by_id(order_id):
        order = Order.objects.filter(id=order_id)
        if order.exists():
            order.delete()
            return True
        return False
