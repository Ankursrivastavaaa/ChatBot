## intent:greet
- hey.
- hello.
- hi.
- hey there.
- Heyyy
- hey !!!!!
- Holaa
- Hi
- Hola
- Hey
- Hello !!
- Hello!

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
- yes
- yes. Please

## intent:deny
- no
- never
- I don't think so
- don't like that
- no way
- not really
- No
- no thanks
- no. thanks

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
- Im hungry. Looking out for some good restaurants
- [bengaluru](location:bangalore)
- [chinese](cuisine)
- [less than 300](budget:low)
- Can you suggest some good restaurants in [Rishikesh](location)
- Okay. Show me some in [Allahabad](location)
- Okay. Show me some in [Pune](location)
- I am looking for [Mexican](cuisine)
- [300 to 700](budget:medium)
- Can you suggest some good restaurants in [kolkata](location)
- [american](cuisine)
- [<300](budget:low)
- in mubaim
- [Mumbai](location)
- Im hungry. Looking out for some good [chinese](cuisine) restaurants in [chandigarh](location)
- [more than 700](budget:high)
- Get me a resturant
- [mankapur](location)
- [agra](location)
- [Italian](cuisine)
- [costly](budget:high) one

## intent:send_email
- yes send it to [abc@gmail.com](email)
- [ankur@gmail.com](email)
- Yes send it to [ankursrivastavaaa@gmail.com](email)
- [android@domain.com](email)

## synonym:300-700
- between 300 to 700
- between 300 - 700
- moderate priced
- not very high
- middle class

## synonym:4
- four

## synonym:Delhi
- New Delhi

## synonym:bangalore
- bengaluru
- Bengaluru

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:high
- more than 700
- costly
- expensive
- top
- best one

## synonym:low
- less than 300
- <300
- cheap
- cheapest
- low bugdet

## synonym:medium
- 300 to 700
- midium
- between 300-700
- 300-700

## regex:email
- ^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$

## regex:greet
- hey[^\s]*

## lookup:location
  data/locations.txt

## lookup:location
  data/allLocations.txt
