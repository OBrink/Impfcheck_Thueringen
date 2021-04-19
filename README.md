# Impfcheck_Thueringen
This repository contains a very simple script that checks every 10 minutes 
if the Thuringian vaccination information site has changed since the last check.
If any changes are detected, it will make create a pop-up message to notify you.

### Get started
- Clone this repository.


    git clone https://github.com/OBrink/Impfcheck_Thueringen

- You might need to install beautifulsoup:

    
    pip install beautifulsoup4


Simply run 


    python  impf_checker.py

The script will then run for 10 hours and check every 10 minutes if 
something has changed since the last check. The text from the page 
is saved in impfen_thueringen.txt in same directory.
