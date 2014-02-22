from datetime import timedelta, datetime

from django.db import models

class Client(models.Model):
    """
    Creating a client instance

    >>> a_client = Client.objects.create(name='david', email='david6116@yahoo.com', phone=7706338574, comments='optional')
    >>> a_client.name
    'david'
    >>>
    """
    name = models.CharField(max_length=128)
    email = models.EmailField(max_length=128)
    phone = models.CharField(max_length=20)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class Project(models.Model):

    client = models.ForeignKey(Client, related_name='projects')
    name = models.CharField(max_length=128)
    rate = models.FloatField(default=0.00)
    comments = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    def summary(self):
        """
        Summary takes an instance of a Project and returns the total
        a mount of time spent on that Project as a timedelta.

       """
        sum_total = timedelta(0)
        project_req_logs = Log.objects.filter(project=self)

        for each_item in project_req_logs:
            sum_total += each_item.duration

        return sum_total

class Contractor(models.Model):
    name = models.CharField(max_length=128)
    rate = models.FloatField()
    projects = models.ManyToManyField(Project, related_name='contractors', blank=True)
    user = models.OneToOneField('auth.User', null=True)

    def __unicode__(self):
        return self.name

class Log(models.Model):
    contractor = models.ForeignKey(Contractor)
    project = models.ForeignKey(Project)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True)

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return u'%s, %s, %s, %s' % (self.contractor, self.project, self.start_time, self.end_time)

    @property
    def duration(self):
        """
        Takes a log instance and calculates the time spent on a project
        the log can still be active or can be a completed log.

        >>> log = Log(start_time=datetime(2012, 4, 6, 18, 44, 10, 998637),
        ...             end_time=datetime(2012, 4, 6, 18, 46, 8, 386904))
        >>> log.duration
        datetime.timedelta(0, 117, 388267)
        """


        if self.end_time is None:
            difference = datetime.now() - self.start_time
        else:
            difference = self.end_time - self.start_time
        return difference

    def stop(self):
        assert(self.end_time is None)
        self.end_time = datetime.now()
        self.save()

    @classmethod
    def start(cls, project, contractor, comments=""):
        try:
            Log.objects.get(contractor=contractor, end_time=None)
            raise Exception('hey stupid your log isnt instantiating')

        except Log.DoesNotExist:
            new_log = Log(project=project, contractor=contractor, start_time=datetime.now(), comments=comments)
            new_log.start_time = datetime.now()
            new_log.save()
            return new_log
