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


# First, define the Manager subclass.
class DahlBookManager(models.Manager):
    def get_query_set(self):
        return super(DahlBookManager, self).get_query_set().filter(author='Roald Dahl') #get_query_set == Book.objects.all()

class BookManager(models.Manager):
    def title_count(self, keyword):
        return self.filter(title__icontains=keyword).count()

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    objects = models.Manager() # The default manager.**
    dahl_objects = DahlBookManager() # The Dahl-specific manager.**

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

from django.db import connection, models

class PersonManager(models.Manager):
    def first_names(self, last_name):
        cursor = connection.cursor()
        cursor.execute("""
            SELECT DISTINCT first_name
            FROM people_person
            WHERE last_name = %s""", [last_name])
        return [row[0] for row in cursor.fetchone()]

from django.contrib.localflavor.us.models import USStateField

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    objects = PersonManager()
    birth_date = models.DateField()
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = USStateField() # Yes, this is U.S.-centric...

    def baby_boomer_status(self):
        "Returns the person's baby-boomer status."
        import datetime
        if datetime.date(1945, 8, 1) <= self.birth_date <= datetime.date(1964, 12, 31):
            return "Baby boomer"
        if self.birth_date < datetime.date(1945, 8, 1):
            return "Pre-boomer"
        return "Post-boomer"

    def is_midwestern(self):
        "Returns True if this person is from the Midwest."
        return self.state in ('IL', 'WI', 'MI', 'IN', 'OH', 'IA', 'MO')

    def _get_full_name(self):
        "Returns the person's full name."
        return u'%s %s' % (self.first_name, self.last_name)
    full_name = property(_get_full_name)

