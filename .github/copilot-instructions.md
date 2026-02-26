# Title
Honkai Star Rail Promo Code Scraper
# Description
This program scrapes promo codes for the game Honkai Star Rail,
eventually it will be updated to also be used for other games and other links but for now Star Rail is fine.
# Input
Data from the site Game8 (https://game8.co/games/Honkai-Star-Rail/archives/410296)
# Output
A Json file fromatted in a way that shows:
- The date of the scraping
- the promo code
- The link to redeem 
- the rewards 
- the image of the reward

E.G. 
{
   "Data": "26-02-2026",
   "Codice": "placehodler",
   "Link": "https://whatever.test",
   "Rewards": [
       {"img": "https://whatever.test", "Name": "placeholder", "Quantity": 10},
       {"img": "https://whatever.test", "Name": "placeholder", "Quantity": 10}
   ]
}
# Logging
Use the logging module that python provides along with the logconfig() function in [functions.py](../src/functions.py),
it should be called at the start of execution along with a message like ("Inizio Programma").
All the logging should be done in Italian.
# Docs
All the docs, commits, comments, docstrings and in general anything that is not code should be in Italian,
function names, variables, classes and other code is fine in english.
# Compiling
Compile using the [buildEXE.bat](../scripts/buildEXE.bat) file
