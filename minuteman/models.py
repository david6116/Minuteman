from datetime import *

from django.db import models

# This comment space is needed for random stuff

class Client(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20)
    comments = models.TextField()

    def __unicode__(self):
        return self.name

class Project(models.Model):
    client = models.ForeignKey(Client, related_name='projects')
    name = models.CharField(max_length=128)
    rate = models.FloatField()
    comments = models.TextField()

    def __unicode__(self):
        return self.name

    def summary(self):

        sum_total = timedelta(0)
        project_req_logs = Log.objects.filter(project=self)

        for each_item in project_req_logs:
            sum_total += each_item.duration

        return sum_total





class Contractor(models.Model):
    name = models.CharField(max_length=128)
    rate = models.FloatField()
    projects = models.ManyToManyField(Project)
    user = models.OneToOneField('auth.User', null=True)

    def __unicode__(self):
        return self.name

    #contractor, project, start, stop
class Log(models.Model):
    contractor = models.ForeignKey(Contractor)
    project = models.ForeignKey(Project)
    start = models.DateTimeField()
    stop = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('start',)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.contractor, self.project, self.start, self.stop)

    @property
    def duration(self):

        if self.stop is None:
            difference = datetime.now() - self.start
        else:
            difference = self.stop - self.start
        return difference



