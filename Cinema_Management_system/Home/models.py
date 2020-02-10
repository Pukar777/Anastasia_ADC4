from django.db import models


# Create your models here.
class Movie(models.Model):
	Movie_title = models.CharField(max_length=30)
	Movie_genre = models.CharField(max_length=30)
	Movie_price = models.DecimalField(max_digits=5, decimal_places=2)
	Movie_image = models.ImageField(blank=True, null=True, upload_to="movies/images")
	def __str__(self):
		return self.Movie_title

class Customer(models.Model):
	Customer_Firstname = models.CharField(max_length=30)
	Customer_Lastname = models.CharField(max_length=30)
	Customer_Username = models.CharField(max_length=30)
	Customer_email = models.EmailField(max_length=50)
	movie = models.ForeignKey(Movie, on_delete= models.CASCADE)


	def __str__(self):
		return self.Customer_Username

		
class Booking(models.Model):
	Booking_ticketCount = models.IntegerField()
	Booking_price = models.DecimalField(max_digits=9, decimal_places=2)
	Movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE)
	Customer_Username = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return self.Booking_ticketCount

