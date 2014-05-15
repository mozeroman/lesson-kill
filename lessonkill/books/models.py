from django.db import models
from datetime import datetime

class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    #logintime = models.TimeField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['-name']

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(blank = True, verbose_name = 'e-mail')

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title

class Account(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 20)
    signature = models.CharField(max_length = 100, blank = True, default = "The guy is too lazy to leave nothing")
    #signin_time = models.DateTimeField()
    #lgtime = models.DateField()
    #logintime = models.DateTimeField(blank = True)
    #logintime = models.datetime
    #logintime = models.DateTimeField(default = datetime.now, blank = True)
    logintime = models.DateTimeField(auto_now = True, blank = True)

    def __unicode__(self):
        return u'%s     %s     %s' % (self.username, self.signature, self.logintime)

