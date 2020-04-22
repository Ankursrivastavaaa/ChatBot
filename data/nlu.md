## intent:greet
- hey.
- hello.
- hi.
- hey there. How can i help you ?
- Heyyy

## intent:goodbye
- bye
- goodbye
- see you around
- see you later

## intent:affirm
- yesrasa
- indeed
- of course
- that sounds good
- correct

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really

## intent:mood_great
- perfect
- very good
- great
- amazing
- wonderful
- I am feeling very good
- I am great
- I'm good

## intent:mood_unhappy
- sad
- very sad
- unhappy
- bad
- very bad
- awful
- terrible
- not very good
- extremely sad
- so sad

## intent:bot_challenge
- are you a bot?
- are you a human?
- am I talking to a bot?
- am I talking to a human?

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- Find me a restaurants in [Bangalore](location).
- Get me a restaurants in [Hyderabad](location).
- looking for a resturant in [Kolkata](location).
- i am hungry looking for resturant
- in [pune](location)
- i am looking for [chinese](cuisine)
- [300-700](budget)

## intent:send_email
- yes send it to [abc@gmail.com](email)

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:mid
- moderate

## synonym:vegetarian
- veggie
- vegg

## regex:email
- ^\\w+(\\w+)*\\@(\\w+)*\\.(\\w+)*(.(\\w+)*)?$"

## regex:greet
- hey[^\s]*

## lookup:location
  data/locations.txt
