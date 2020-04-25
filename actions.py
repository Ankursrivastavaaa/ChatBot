from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
from numpy import loadtxt
import zomatopy
import json
import smtplib
from email.message import EmailMessage
from concurrent.futures import ThreadPoolExecutor
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import Restarted

from rasa_sdk import Action
from rasa_sdk.events import SlotSet

d_email_rest = []

class RestaurantForm(FormAction):
    """custom form action"""

    def name(self) -> Text:
        return "restaurant_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location", "cuisine", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cuisine": self.from_entity(entity="cuisine", intent="request_restaurant"),
            "location": self.from_entity(entity="location", intent="request_restaurant"),
            "budget": self.from_entity(entity="budget", intent="request_restaurant"),
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def cuisine_db() -> List[Text]:
        return [
            "chinese",
            "italian",
            "south indian",
            "north indian",
            "american",
            "mexican",
        ]
    @staticmethod
    def location_db() -> List[Text]:
        location_list = loadtxt("data/locations.txt",dtype=str, delimiter="\n", unpack=False)
        return location_list

    def validate_location(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("Location:",value)
        if isinstance(value, list):
            value = value[0] 
        if value.lower() in self.location_db():
            return {"location": value}
        else:
            dispatcher.utter_message(template="utter_wrong_location")
            return {"location": None}
    # USED FOR DOCS: do not rename without updating in docs
    def validate_cuisine(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""
        print("Cusisine:",value)
        if isinstance(value, list):
            value = value[0] 
        if value.lower() in self.cuisine_db():
            return {"cuisine": value}
        else:
            dispatcher.utter_message(template="utter_wrong_cuisine")
            return {"cuisine": None}

    def validate_budget(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        print("Budget:",value)
        if isinstance(value, list):
            value = value[0] 
        if value.lower() in ["low","mid","high"]:
            return {"budget": value}
        else:
            dispatcher.utter_message(template="utter_wrong_budget")
            return {"budget": None}


    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}
        zomato = zomatopy.initialize_app(config)
        actionListener = tracker.get_slot("actionListener")
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        print(cuisine,budget,loc)
        return []
        # results, lat, lon = self.get_location_suggestions(loc,zomato)

    #     if (results == 0):
    #         # Zomato API could not find suggestions for this location.
    #         restaurant_exist = False
    #         dispatcher.utter_message("Sorry, no results found in this location:("+ "\n")
    #     else:
    #         d_rest = self.get_restaurants(lat, lon, cuisine)
            
    #         d_budget_rating_sorted = sorted(
    #                 d_rest, key=lambda k: k['restaurant']['user_rating']['aggregate_rating'], reverse=True)

    #         # Build the response
    #         response = ""
    #         restaurant_exist = False
    #         if len(d_budget_rating_sorted) == 0:
    #             dispatcher.utter_message("Sorry, no results found :("+ "\n")
    #         else:
    #             # Pick the top 5
    #             d_budget_rating_top5 = d_budget_rating_sorted[:5]
    #             global d_email_rest
    #             d_email_rest = d_budget_rating_sorted[:10]
    #             if(d_email_rest and len(d_email_rest) > 0):
    #                 restaurant_exist = True
    #             for restaurant in d_budget_rating_top5:
    #                 response=response+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n" + " has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"
                
    #             dispatcher.utter_message("-----"+response)
    #     return [SlotSet('location',loc)]

    # def get_location_suggestions(self, loc, zomato):
    #     # Get location details including latitude and longitude
    #     location_detail = zomato.get_location(loc, 1)
    #     d1 = json.loads(location_detail)
    #     lat = 0
    #     lon = 0
    #     results = len(d1["location_suggestions"])
    #     if (results > 0):
    #         lat = d1["location_suggestions"][0]["latitude"]
    #         lon = d1["location_suggestions"][0]["longitude"]
    #     return results, lat, lon

    # def get_restaurants(self, lat, lon, cuisine):
    #     cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
    #                         'mexican': 73, 'north indian': 50, 'south indian': 85}
    #     d_rest = []
    #     executor = ThreadPoolExecutor(max_workers=5)
    #     for res_key in range(0, 101, 20):
    #         executor.submit(retrieve_restaurant, lat, lon, cuisines_dict, cuisine, res_key, d_rest)
    #     executor.shutdown()
    #     return d_rest

    # def retrieve_restaurant(self ,lat, lon, cuisines_dict, cuisine, res_key, d_rest):
    #     base_url = "https://developers.zomato.com/api/v2.1/"
    #     headers = {'Accept': 'application/json',
    #                 'user-key': '5787bb8301dd97fbe86ec40febf7e03b'}
    #     try:
    #         results = (requests.get(base_url + "search?" + "&lat=" + str(lat) + "&lon=" + str(lon) + "&cuisines=" + str(
    #             cuisines_dict.get(cuisine)) + "&start=" + str(res_key)+"&count=20", headers=headers).content).decode("utf-8")
    #     except:
    #         return
    #     d = json.loads(results)
    #     d_rest.extend(d['restaurants'])
    
    
   

# Send email the list of 10 restaurants
class ActionSendEmail(Action):
    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_email = tracker.get_slot('email')

        # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        print(cuisine,budget,loc,to_email)
        return [AllSlotsReset()]
        # global d_email_rest
        # email_rest_count = len(d_email_rest)
        # # Construct the email 'subject' and the contents.
        # d_email_subj = "Top " + str(email_rest_count) + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        # d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n"
        # for restaurant in d_email_rest:
        #     d_email_msg = d_email_msg + restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+" has been rated " + restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" +"\n"

        
        # # Open SMTP connection to our email id.
        # s = smtplib.SMTP("smtp.gmail.com", 587)
        # s.starttls()
        # s.login("neerajankurchatbotproject@gmail.com", "iiitbchatbot")

        # # Create the msg object
        # msg = EmailMessage()

        # # Fill in the message properties
        # msg['Subject'] = d_email_subj
        # msg['From'] = "neerajankurchatbotproject@gmail.com"

        # # Fill in the message content
        # msg.set_content(d_email_msg)
        # msg['To'] = to_email

        # s.send_message(msg)
        # s.quit()
        # dispatcher.utter_message("**** EMAIL SENT! HAPPY DINING :) ****")

   