from django.db import models

# Create your models here.
class Movie(models.Model):
	Movie_title = models.CharField(max_length=30)
	Movie_License = models.CharField(max_length=50, primary_key=True)
	Movie_genre = models.CharField(max_length=30)
	Movie_releaseDate = models.DateField(editable=False)
	Movie_finalShowDate = models.DateField(editable=True)

	def __str__(self):
		return self.Movie_License