from django.db import models

AGENCIES = (
    ('P', 'Police'),
    ('T', 'Transportation'),
    ('F', 'Fire'),
    ('H', 'Health'),
    ('S', 'Sanitation'),
    ('U', 'Utilities'),
    ('O', 'Other'),
)

class Report(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField('Date Filed')
    description = models.TextField(max_length=250)
    location = models.CharField(max_length=50)
    agency = models.CharField(
        max_length=1,
        choices= AGENCIES,
        default= [0][0]
    )

    def __str__(self):
        return f'{self.title} ({self.id})'
