from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
from numpy import loadtxt


config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		# cuisine = tracker.get_slot('cuisine')
		cuisine = 'biryani'
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'bakery':5,'chinese':25,'cafe':30,'italian':55,'biryani':7,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 5)
		d = json.loads(results)
		response=""
		if d['results_found'] == 0:
			response= "no results"
		else:
			for restaurant in d['restaurants']:
				response=response+ "Found "+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"
		
		dispatcher.utter_message("-----"+response)
		return [SlotSet('location',loc)]



# Check if the location exists, else utter not found.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_check_location'

	def run(self, dispatcher, tracker, domain):
		location_list = loadtxt("data/locations.txt",dtype=str, delimiter="\n", unpack=False)
		loc = tracker.get_slot('location')

		city = str(loc)
		print(city)
		if(city.lower() not in location_list):
			dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
		return
		
			


# Send email the list of 10 restaurants
class ActionSendEmail(Action):
	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		email = tracker.get_slot('email')
		
		print(email)
		#return [AllSlotsReset()]


