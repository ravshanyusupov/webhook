from django.db import models


class Kimyo(models.Model):
    question = models.TextField()
    a_answer = models.CharField(max_length=255)
    b_answer = models.CharField(max_length=255)
    c_answer = models.CharField(max_length=255)
    d_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question


class Users(models.Model):
    username = models.CharField(max_length=255)
    test_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username




