from django.db import models


# * makemigrations - Create changes & Store in a file
# * migrate - Apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):

    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    # Display the name of the object in the admin panel
    def __str__(self):
        return f"{self.name} - {self.email}"
