from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50) # [cite: 140]
    last_name = models.CharField(max_length=50)  # [cite: 140]
    birth = models.DateField()                  # [cite: 140]

    def __str__(self):
        return f"Musician (id={self.id}, last_name={self.last_name})" # [cite: 299]

class Venue(models.Model):
    name = models.CharField(max_length=20) # [cite: 827]

    def __str__(self):
        return f"Venue(id={self.id}, name={self.name})" # [cite: 827]

class Room(models.Model):
    name = models.CharField(max_length=20) # [cite: 827]
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE) # [cite: 827, 828]

    def __str__(self):
        return f"Room(id={self.id}, name={self.name})" # [cite: 827]

class Band(models.Model):
    name = models.CharField(max_length=20) # [cite: 960]
    musicians = models.ManyToManyField(Musician) # [cite: 960]

    def __str__(self):
        return f"Band(id={self.id}, name={self.name})" # [cite: 960]python manage.py makemigrations bands