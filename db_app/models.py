from django.db import models


class UserDetails(models.Model):
    firstname = models.TextField()
    middlename = models.TextField()
    lastname = models.TextField()
    dateofbirth = models.DateField()
    
    def __str__(self):
        return f"{self.firstname}, {self.middlename}, {self.lastname}"
