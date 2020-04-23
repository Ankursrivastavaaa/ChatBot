
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

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": ">700"}
    - slot{"budget": ">700"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - utter_ask_for_email_to_send
* send_email{"email": "asjn@domain.com"}
    - slot{"email": "asjn@domain.com"}
    - action_send_email
    - utter_email_sent

## interactive_story_1
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "300-700"}
    - slot{"budget": "300-700"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_check_location
* restaurant_search{"location": "mankapur"}
    - slot{"location": "mankapur"}
    - action_check_location
* restaurant_search
    - action_check_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_check_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "<300"}
    - slot{"budget": "<300"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_for_email_to_send
* send_email{"email": "anch@gmail.com"}
    - slot{"email": "anch@gmail.com"}
    - action_send_email
    - utter_email_sent
