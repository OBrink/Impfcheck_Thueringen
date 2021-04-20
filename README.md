# Impfcheck_Thueringen
This repository contains a very simple script that checks every 5-15 minutes 
if the Thuringian vaccination information site (https://www.impfen-thueringen.de/terminvergabe.html) has changed since the last check.
If any changes are detected, it creates a pop-up message as a notification..

### Get started
- Clone this repository.


    git clone https://github.com/OBrink/Impfcheck_Thueringen

- You might need to install beautifulsoup:

    
    pip install beautifulsoup4


- Simply run 


    python  impf_checker.py

The script will then run for approximately 10 hours and check every 5-15 minutes if 
something has changed since the last check. The text from the page 
is saved in impfen_thueringen.txt in the same directory.
