from django.db import models

# Create your models here.

# Job types
JOB_TYPES = (
    ('Full time', 'Full time'),
    ('Part time', 'Part time'),
)

class Job(models.Model):
    title = models.CharField(max_length=150)
    # location
    job_type = models.CharField(max_length=15, choices=JOB_TYPES)
    description = models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experience = models.IntegerField(default=1)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
