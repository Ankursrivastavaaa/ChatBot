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
import smtplib
from email.message import EmailMessage
from concurrent.futures import ThreadPoolExecutor

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




# Send email the list of 10 restaurants
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        
		#cuisine = tracker.get_slot('cuisine')
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
        
        # Get user's email id
        to_email = tracker.get_slot('email')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        
		# Construct the email 'subject' and the contents.
        d_email_subj = "Top 5" + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n" + response
        
        # Open SMTP connection to our email id.
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login("neerajankurchatbotproject@gmail.com", "iiitbchatbot")

        # Create the msg object
        msg = EmailMessage()

        # Fill in the message properties
        msg['Subject'] = d_email_subj
        msg['From'] = "neerajankurchatbotproject@gmail.com"

        # Fill in the message content
        msg.set_content(d_email_msg)
        msg['To'] = to_email

        s.send_message(msg)
        s.quit()
        dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")
        return []


# Check if the location exists, else utter not found.
class ActionValidateLocation(Action):
	def name(self):
		return 'action_validate_location'

	def run(self, dispatcher, tracker, domain):
		location_list = loadtxt("data/locations.txt",dtype=str, delimiter="\n", unpack=False)
		loc = tracker.get_slot('location')

		city = str(loc)
		print(city)
		if(city.lower() not in location_list):
			dispatcher.utter_message(template="utter_wrong_location")
        
# Check if the location exists, else utter not found.
class ActionValidateBudget(Action):
	def name(self):
		return 'action_validate_budget'

	def run(self, dispatcher, tracker, domain):
		bud = tracker.get_slot('budget')
		budget = str(bud)
		print(budget)
		budget_list = ["low","medium","high"]
		if(budget.lower() not in budget_list):
			dispatcher.utter_message(template="utter_wrong_budget")

# Check if the location exists, else utter not found.
class ActionValidateCuisine(Action):
	def name(self):
		return 'action_validate_cuisine'

	def run(self, dispatcher, tracker, domain):
		cus = tracker.get_slot('cuisine')
		cuisine = str(cus)
		print(cuisine)
		cuisine_list = ["chinese","italian","south indian","north indian","american","mexican"]
		if(cuisine.lower() not in cuisine_list):
			dispatcher.utter_message(template="utter_wrong_cuisine")