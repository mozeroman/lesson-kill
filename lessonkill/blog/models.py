from django.db import models

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    #timestamp = models.DateTimeField(auto_now = True)
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ['-timestamp']
    def __unicode__(self):
        return u'%s %s' % (self.title, self.timestamp)


