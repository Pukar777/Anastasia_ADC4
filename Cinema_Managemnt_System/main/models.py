from django.db import models

# Create your models here.

class Customer(models.Model):
	Customer_name = models.CharField(max_length=30)
	Customer_id = models.CharField(max_length=7, primary_key=True)
	Customer_address = models.CharField(max_length=50, blank=True)
	Customer_contactNo = models.IntegerField()

	def __str__(self):
		return self.Customer_name


class Cinema(models.Model):
	Cinema_name = models.CharField(max_length=30, primary_key=True)
	Cinema_address = models.CharField(max_length=50, blank=True)
	Cinema_email = models.EmailField(max_length=50)
	Cinema_admin = models.CharField(max_length=30, default='Admin')

	def __str__(self):
		return self.Cinema_name

class Movie(models.Model):
	Movie_title = models.CharField(max_length=30)
	Movie_License = models.CharField(max_length=50, primary_key=True)
	Movie_genre = models.CharField(max_length=30)
	Movie_releaseDate = models.DateField(editable=False)
	Movie_finalShowDate = models.DateField(editable=True)

	def __str__(self):
		return self.Movie_License

class Booking(models.Model):
	Booking_price = models.DecimalField(max_digits=9, decimal_places=2)
	Booking_seat = models.CharField(max_length=4)
	Booking_showTime = models.DateTimeField(auto_now=False,auto_now_add=False)
	Booking_id = models.CharField(max_length=7, primary_key=True)
	Booking_ticketCount = models.IntegerField()
	Movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
	Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)

	def __str__(self):
		return self.Booking_id

class Payment(models.Model):
	Payment_id = models.CharField(max_length=9, primary_key=2)
	Payment_totalPrice = models.DecimalField(max_digits=7,decimal_places=2)
	Customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
	Booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)
	Payment_date = models.DateTimeField()

	def __str__(self):
		return self.Payment_id

		


		
		