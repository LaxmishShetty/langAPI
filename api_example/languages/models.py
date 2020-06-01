from django.db import models


class Paradigm(models.Model):
    """Paradigms of different programming languages"""
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Language(models.Model):
    """Language model for the API"""
    name = models.CharField(max_length=50)
    paradigm = models.ForeignKey(Paradigm, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the above model"""
        return self.name


class Programmers(models.Model):
    """List of programmers who know many languages"""
    name = models.CharField(max_length=50)
    languages = models.ManyToManyField(Language)

    def __str__(self):
        return self.name
