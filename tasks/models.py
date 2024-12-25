from django.db import models


class Task(models.Model):
    STATUSES = {
        'draft': 'Drafts',
        'in progress': 'In Progress',
        'completed': 'Completed'
    }

    name = models.CharField(max_length=100)
    status = models.TextField(choices=STATUSES)
    description = models.TextField(max_length=200)
    """
    name: String
    status: string choicefield ['draft', 'in progress', 'completed']
    description: string
    """