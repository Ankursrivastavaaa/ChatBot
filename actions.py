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

d_email_rest = []

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
    
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        results, lat, lon = self.get_location_suggestions(loc,zomato)

        if (results == 0):
            # Zomato API could not find suggestions for this location.
            restaurant_exist = False
            dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
        else:
            d_rest = self.get_restaurants(lat, lon, cuisine)
            
            d_budget_rating_sorted = sorted(
                    d_rest, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

            # Build the response
            response = ""
            restaurant_exist = False
            if len(d_budget_rating_sorted) == 0:
                dispatcher.utter_message("Sorry, no results found :("+ "\n")
            else:
                # Pick the top 5
                d_budget_rating_top5 = d_budget_rating_sorted[:5]
                global d_email_rest
                d_email_rest = d_budget_rating_sorted[:10]
                if(d_email_rest and len(d_email_rest) > 0):
                    restaurant_exist = True
                for restaurant in d_budget_rating_top5:
                    response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n" + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
                
                dispatcher.utter_message("-----"+response)
        return [SlotSet('location',loc)]
    
    def get_location_suggestions(self, loc, zomato):
        # Get location details including latitude and longitude
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = 0
        lon = 0
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat = d1["location_suggestions"][0]["latitude"]
            lon = d1["location_suggestions"][0]["longitude"]
        return results, lat, lon

    def get_restaurants(self, lat, lon, cuisine):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        d_rest = []
        executor = ThreadPoolExecutor(max_workers=5)
        for res_key in range(0, 101, 20):
            executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
        executor.shutdown()
        return d_rest



# Send email the list of 10 restaurants
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'
    
    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('emailid')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        global d_email_rest
        email_rest_count = len(d_email_rest)
        # Construct the email 'subject' and the contents.
        d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        for restaurant in d_email_rest:
            d_email_msg = d_email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        
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


def retrieve_restaurant(lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    base_url = "https://developers.zomato.com/api/v2.1/"
    headers = {'Accept': 'application/json',
                'user-key': '5787bb8301dd97fbe86ec40febf7e03b'}
    try:
        results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
            cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    except:
        return
    d = json.loads(results)
    d_rest.extend(d['restaurants'])