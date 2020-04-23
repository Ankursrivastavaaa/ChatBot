## intent:greet
- hey.
- hello.
- hi.
- hey there.
- Heyyy
- hey !!!!!
- Holaa

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
- No
- no thanks

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
- get me [Mexican](cuisine)
- [Italian](cuisine)
- Search for [American](cuisine)
- looking for [South Indian](cuisine)
- get me [North Indian](cuisine)
- I’ll prefer [Italian](cuisine)!
- [<300](budget)
- [300-700](budget)
- [>700](budget)
- find me a resturant
- [Agra](location)
- [Mexican](cuisine)
- [cheap](budget:<300)
- Can you suggest some good restaurants in [Agra](location)
- [chines](cuisine:chinese)
- [costly](budget:>700)
- Can you suggest some good restaurants in [Rishikesh](location)
- [Pune](location)
- [South Indian](cuisine)
- Im hungry. Looking out for some good restaurants
- [bengaluru](location:bangalore)
- ill prefer [North Indian](cuisine)
- >[less than 300](budget:<300)
- Can you suggest some good restaurants in [Rishikesh](location)
- Please look in [mankapur](location)
- ok, find me in abcssa
- [Delhi](location)
- [Mexican](cuisine)
- [cheapest](budget:<300)

## intent:send_email
- yes send it to [abc@gmail.com](email)
- send to [ankur@yahoo.com](email)
- [ankursrivastava2@deloitte.com](email)
- Yes. Please to [testing@upgrad.com](email)
- send to [asjn@domain.com](email)
- [anch@gmail.com](email)

## synonym:300-700
- between 300 to 700
- between 300 - 700
- moderate priced
- not very high
- middle class

## synonym:4
- four

## synonym:<300
- cheap
- less than 300
- cheapest
- low bugdet

## synonym:>700
- costly
- more than 700
- expensive
- top
- best one

## synonym:Delhi
- New Delhi

## synonym:bangalore
- bengaluru
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
- ^\w+([-+.']\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$

## regex:greet
- hey[^\s]*

## lookup:location
  data/locations.txt
