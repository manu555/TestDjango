from django.db import models
from django.utils import timezone

class Project(models.Model):
    Subject = models.CharField(max_length=200)
    Description = models.TextField()
    Handler = models.ForeignKey('auth.User')
    # requester = models.ForeignKey('Customer')
    # assignee = models.ForeignKey('Collaborator')
    created_date = models.DateTimeField(default=timezone.now)
    last_updated_date = models.DateTimeField(blank=True, null=True)

    def open(self):
        self.created_date = timezone.now()
        self.save()

    def update(self, text=None):
        if text != None:
            self.Description = text
        self.last_updated_date = timezone.now()

    def __init__(self):
        super(Project, self).__init__()
        self.Subject = 'Please enter subject here!'
        self.Description = 'Please enter description here!'
        self.last_updated_date = None

    def __str__(self):
        return self.Subject






# Create your models here.
