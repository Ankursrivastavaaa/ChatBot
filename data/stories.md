## happy path
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email
    - email_form
    - form{"name": "email_form"}
    - form{"name": null}

## happy path 2
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - form{"name": null}
    - utter_ask_for_email_to_send
* deny
    - action_reset_slots
    - utter_email_not_sent


## interactive_story_1
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: request_restaurant{"location": "chennai"}
    - form: restaurant_form
    - slot{"location": "chennai"}
    - slot{"requested_slot": "cuisine"}
* form: request_restaurant{"cuisine": "Italian"}
    - form: restaurant_form
    - slot{"cuisine": "Italian"}
    - slot{"requested_slot": "budget"}
* form: request_restaurant{"budget": "300-700"}
    - form: restaurant_form
    - slot{"budget": "300-700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* send_email{"email": "abcdgdk@dkj.com"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email": "abcdgdk@dkj.com"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_2
* greet
    - utter_greet
* request_restaurant{"location": "Pakistan"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": null}
    - slot{"requested_slot": "location"}
* form: request_restaurant{"location": "delhi"}
    - form: restaurant_form
    - slot{"location": "delhi"}
    - slot{"requested_slot": "cuisine"}
* form: request_restaurant{"cuisine": "American"}
    - form: restaurant_form
    - slot{"cuisine": "American"}
    - slot{"requested_slot": "budget"}
* form: request_restaurant{"budget": "700"}
    - form: restaurant_form
    - slot{"budget": "700"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* send_email{"email": "xyz@sth.edu"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email": "xyz@sth.edu"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_3
* request_restaurant{"location": "kolkata"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "kolkata"}
    - slot{"requested_slot": "cuisine"}
* form: request_restaurant{"cuisine": "South Indian"}
    - form: restaurant_form
    - slot{"cuisine": "South Indian"}
    - slot{"requested_slot": "budget"}
* form: request_restaurant{"budget": "300"}
    - form: restaurant_form
    - slot{"budget": "300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "jddk.2jmd@kdl.co.in"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_4
* greet
    - utter_greet
* request_restaurant
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"requested_slot": "location"}
* form: request_restaurant{"location": "mumbai"}
    - form: restaurant_form
    - slot{"location": "mumbai"}
    - slot{"requested_slot": "cuisine"}
* form: request_restaurant{"cuisine": "Italian"}
    - form: restaurant_form
    - slot{"cuisine": "Italian"}
    - slot{"requested_slot": "budget"}
* form: request_restaurant{"budget": "300"}
    - form: restaurant_form
    - slot{"budget": "300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* affirm
    - utter_ask_email_address
* send_email{"email": "jddk.2jmd@kdl.co.in"}
    - email_form
    - form{"name": "email_form"}
    - slot{"email": "jddk.2jmd@kdl.co.in"}
    - form: reset_slots
    - form{"name": null}
    - slot{"requested_slot": null}

## interactive_story_5
* request_restaurant{"cuisine": "chinese", "location": "chandigarh"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"requested_slot": "budget"}
* form: request_restaurant{"budget": "300"}
    - form: restaurant_form
    - slot{"budget": "300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* deny
    - action_reset_slots
    - reset_slots
    - utter_email_not_sent

## interactive_story_6
* request_restaurant{"cuisine": "South indian", "location": "Pune", "budget": "300"}
    - restaurant_form
    - form{"name": "restaurant_form"}
    - slot{"location": "Pune"}
    - slot{"cuisine": "South indian"}
    - slot{"budget": "300"}
    - form{"name": null}
    - slot{"requested_slot": null}
    - utter_ask_for_email_to_send
* send_email{"email": "neeraj_1395@yahoo.com.hk"}
    - email_form
