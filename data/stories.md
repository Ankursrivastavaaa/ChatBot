## interactive_story_1
* greet
    - utter_greet
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "ankur@gmail.com"}
    - slot{"email": "ankur@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_validate_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "Pune"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_for_email_to_send
* send_email{"email": "ankursrivastavaaa@gmail.com"}
    - slot{"email": "ankursrivastavaaa@gmail.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_validate_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "android@domain.com"}
    - slot{"email": "android@domain.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chandigarh", "cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_validate_cuisine
    - action_validate_location
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mankapur"}
    - slot{"location": "mankapur"}
    - action_validate_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "high"}
    - slot{"budget": "high"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "medium"}
    - slot{"budget": "medium"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* restaurant_search{"location": "Buxar"}
    - slot{"location": "Buxar"}
    - action_validate_location
* restaurant_search{"location": "Amaravati"}
    - slot{"location": "Amaravati"}
    - action_validate_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - action_validate_location
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "ank@fro.com"}
    - slot{"email": "ank@fro.com"}
    - action_send_email

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_validate_location
    - utter_ask_location
    - utter_ask_cuisine
* action_search_restaurants{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - action_validate_cuisine
    - utter_ask_budget
* restaurant_search{"budget": "low"}
    - slot{"budget": "low"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_validate_location
    - utter_ask_cuisine
* action_search_restaurants{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - action_validate_cuisine
    - utter_ask_budget
* action_search_restaurants{"budget": "mid"}
    - slot{"budget": "mid"}
    - action_validate_budget
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_for_email_to_send
* deny
    - utter_email_not_sent
