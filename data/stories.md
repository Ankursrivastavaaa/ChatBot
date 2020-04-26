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

