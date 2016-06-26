from django.db import models

# Create your models here.


class Keys(models.Model):
    STATUS = (
        (0, 'Not issued'),
        (1, 'Issued'),
        (2, 'Repaid')
    )
    key = models.CharField(max_length=6, unique=True, db_index=True)
    status = models.PositiveSmallIntegerField(choices=STATUS, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.key

    class Meta:
        ordering = ('-created',)
