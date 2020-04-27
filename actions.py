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

cost_min=0
cost_max=0
class RestaurantForm(FormAction):
    """custom form action"""

    def name(self) -> Text:
        return "restaurant_form"
    config={ "user_key":"47ef160bda39996b2dbaff7f9fd0e554"}
        
    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["location", "cuisine", "budget"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        return {
            "cuisine": self.from_entity(entity="cuisine", intent="request_restaurant"),
            "location": self.from_entity(entity="location", intent="request_restaurant"),
            "budget": [
                self.from_entity(
                    entity="budget", intent=["request_restaurant"]
                ),
            ]
        }
    @staticmethod
    def is_not_int(string: Text) -> bool:
        """Check if a string is an integer"""
        try:
            int(string)
            return False
        except ValueError:
            return True
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
        if isinstance(value, list):
            value = set(value)
            dum=[]
            for val in value:
                val = val.replace("<","").replace(">","").replace(" ","")
                dum.append(val)
            value = set(dum)
            if(len(value) == 0):
                dispatcher.utter_message(template="utter_wrong_budget")
                return {"budget": None}
            elif(len(value) == 1):
                for val in value:
                    break
                value=val
            
            else:
                value='-'.join(sorted(set(value)))
        print("Budget:",value)
        return {"budget": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        # Get required Slot Values
        loc, cuisine, budget_min, budget_max = self.getSlotValues(tracker)
        print((budget_min))   
        print((budget_max))
        zomato = zomatopy.initialize_app(self.config)
        results, lat, lon = self.getLocation(loc,zomato)
        if(results == 0):
            dispatcher.utter_message("Sorry, no results found in this location")
        else:
            # Hit API to get results
            resturantList = self.getRestaurantsFromAPI(lat, lon, budget_min, budget_max, cuisine,zomato)

        chatResponse=""
        emailResponse=""
        if len(resturantList) == 0:
            chatResponse= "Sorry, no results found."
        else:
            count = 0
            for restaurant in resturantList:
                if(count < 5):
                    chatResponse=chatResponse+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+ " has been rated " + \
                            restaurant['restaurant']['user_rating']['aggregate_rating'] + "\n" + "\n"  
                emailResponse=emailResponse+ restaurant['restaurant']['name']+ " in "+ restaurant['restaurant']['location']['address']+"\n"+ " has been rated " + \
                            restaurant['restaurant']['user_rating']['aggregate_rating'] + " and average budget of "+ str(restaurant['restaurant']['average_cost_for_two']) + "\n"+ "\n"
                count = count + 1
        
        dispatcher.utter_message(chatResponse)
        print(cuisine,budget_min,budget_max,loc)
        return [SlotSet("emailResponse",emailResponse)]
    #Returns Slot Values
    def getSlotValues(self,tracker):
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        budget = tracker.get_slot('budget')
        if budget=='300':
            cost_min=0
            cost_max=300
        elif budget=='300-700':
            cost_min=300
            cost_max=700
        elif budget=='700':
            cost_min=700
            cost_max=1000000
        else:
            try:
                cost_min=0
                try:
                    cost_max=int(budget)
                except:
                    cost_min=int(budget.split("-")[0])
                    cost_max=int(budget.split("-")[1])
            except:
                cost_min=0
                cost_max = 100000
        return loc,cuisine,cost_min,cost_max
    # Returns Location
    def getLocation(self,loc,zomato):
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        results = len(d1["location_suggestions"])
        if (results > 0):
            lat=d1["location_suggestions"][0]["latitude"]
            lon=d1["location_suggestions"][0]["longitude"]
        return results,lat,lon
   
    def getRestaurantsFromAPI(self,lat, lon, budget_min, budget_max, cuisine,zomato):
        cuisines_dict = {'american': 1, 'chinese': 25, 'italian': 55,
                         'mexican': 73, 'north indian': 50, 'south indian': 85}
        resturantList=[]
        startIndex=0
        # Keep Hitting the API till we get 10 resturants in desired budget and other filters
        # Max result returned is 20 for Zomato to hitting API`s in Iteration
        while(len(resturantList) <=10):
            print("Hitting API, startIndex", startIndex)
            print("Budget Constraint", budget_min, budget_max)
            
            results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 20 , 'rating', "desc", start_offset=startIndex)
            json_result= json.loads(results)
            startIndex = startIndex+20
            for resturant in json_result['restaurants']:
                if ((resturant['restaurant']['average_cost_for_two'] > budget_min) & (
                    resturant['restaurant']['average_cost_for_two'] < budget_max)):
                        resturantList.append(resturant)
                if(len(resturantList) == 10):
                            break
            print("Total Resturant found", len(resturantList))
            if(len(resturantList) == 10):
                break          
            
        return resturantList
        
	
class ActionResetSlots(Action):
    def name(self):
        return 'action_reset_slots'

    def run(self, dispatcher, tracker, domain):
        return [AllSlotsReset()]



class EmailForm(FormAction):
    """custom form action for Email"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "email_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["email"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""
        return {
        "email": [self.from_entity(entity="email"), self.from_text(intent="send_email")]  
        }
    # USED FOR DOCS: do not rename without updating in docs
    def validate_email(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate email value."""
        if isinstance(value, list):
            value = value[0] 
        if any(tracker.get_latest_entity_values("email")):
        # entity was picked up, validate slot
            return {"email": value}
        else:
        # no entity was picked up, we want to ask again
            dispatcher.utter_template("utter_no_email", tracker)
            return {"email": None}
    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
           # Get user's email id
        to_email = tracker.get_slot('email')
        emailResponse = tracker.get_slot('emailResponse')
        print(to_email)
	    # Get location and cuisines to put in the email
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        # creates SMTP session 
        s = smtplib.SMTP('smtp.gmail.com', 587)
        
        # start TLS for security 
        s.starttls() 
        
        # Authentication 
        s.login("ankurneerajchatbotproject@gmail.com", "iiitbchatbot")
        
       
        # Create the msg object
        msg = EmailMessage()

	    # Construct the email 'subject' and the contents.
        d_email_subj = "Top 10" + " " + cuisine.capitalize() + " restaurants in " + str(loc).capitalize()
        d_email_msg = "Hi there! Here are the " + d_email_subj + "." + "\n" + "\n" +"\n" + emailResponse

        # Fill in the message properties
        message = 'Subject: {}\n\n{}'.format(d_email_subj, d_email_msg)    
        # sending the mail 
        s.sendmail("ankurneerajchatbotproject@gmail.com", to_email , message) 
        # terminating the session 
        s.quit() 
        dispatcher.utter_message(template="utter_email_sent")
        return [AllSlotsReset()]





