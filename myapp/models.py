from django.db import models


class Kimyo(models.Model):
    question = models.TextField()
    a = models.CharField(max_length=255)
    b = models.CharField(max_length=255)
    c = models.CharField(max_length=255)
    d = models.CharField(max_length=255)

    def str(self):
        return self.question


class Users(models.Model):
    username = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username




