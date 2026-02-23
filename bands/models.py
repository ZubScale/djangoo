from django.db import models

class Musician(models.Model):
    """
    Model representing a musician.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    def __str__(self):
        return f"Musician (id={self.id}, last_name={self.last_name})"

class Venue(models.Model):
    """
    Model representing a venue where bands play.
    """
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"Venue(id={self.id}, name={self.name})"

class Room(models.Model):
    """
    Model representing a room within a venue.
    """
    name = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    def __str__(self):
        return f"Room(id={self.id}, name={self.name})"

class Band(models.Model):
    """
    Model representing a band which consists of multiple musicians.
    """
    name = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician)

    def __str__(self):
        return f"Band(id={self.id}, name={self.name})"
