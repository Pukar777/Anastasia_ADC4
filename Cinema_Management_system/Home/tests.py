from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Customer, Booking
# Create your tests here.

class DataTest(TestCase):
	def setUp(self):

		self.movie = Movie.objects.create(Movie_title = 'avatar', Movie_genre = 'Action', Movie_price = '222', Movie_image = '' );
		self.customer = Customer.objects.create(Customer_Firstname = 'Pukar', Customer_Lastname = 'Khatri', Customer_Username = 'Pukar777', Customer_email = 'Pukarkhatri777@gmail.com', movie = 2);
		self.booking = Booking.objects.create(Booking_ticketCount = 5, Booking_price = 1500)

	def testMovieI(self):
		obj = Movie.objects.get(Movie_title='avatar')
		self.assertEqual(obj.Movie_title, "avatar")

	def testMovieII(self):
		obj = Movie.objects.get(Movie_price = 222)
		self.assertEqual(obj.Movie_price, 222)

	def testCustomerI(self):
		obj = Customer.objects.get(Customer_Firstname = 'Pukar')
		self.assertEqual(obj.Customer_Firstname,  'Pukar')

	def testCustomerII(self):
		obj = Customer.obj.get(Customer_email = 'Pukarkhatri777@gmail.com')
		self.assertEqual(obj.Customer_email, 'Pukarkhatri777@gmail.com')

	def testBookingI(self):
		obj = Booking.obj.get(Booking_price = 1500)
		self.assertEqual(obj.Booking_price, 1500)