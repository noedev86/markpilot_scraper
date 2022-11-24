# markpilot_scraper
## challenge markpilot

__main.py__ : was just the sketch to know how to retrieve data 

__solid_scraper.py__ : contains all the classes used to scrape with bs4 the wolle marketplace

__testing_unit.py__ : manual tester, using the classes but only with a print out

__tester_unit.py__ : using the unitest library made a couple basic test runs

## room for improvements : 
  * connect to a database and call the data class with it to make it more dynamic
  * use a much more optimized class to be able to retrieve data on other pages, I tried with https://www.fischer-wolle.de and it only took the basic brands and descriptions
  getting the prices was much more complicated without overfitting the model

## bilan
took me about 4 hours to build this from scratch, I don't know if it really corresponds to a *SOLID* coded work but trying with other description and brands it worked pretty well, at least on the same website
  
