
## Greet
* greet
    - utter_greet


## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - utter_ask_for_email_to_send
* send_email{"email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - action_send_email
    - utter_email_sent
