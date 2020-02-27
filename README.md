# Pagerduty Oncall Schedule

This is a very basic script I use to check who is on call on Pagerduty. 

## Usage

Just set two vars with PD_TOKEN (you can generate one on your PD account) and the schedule id (you can find it as part of the link to your schedule). 
    
    $ PD_TOKEN=************** SCHEDULE=ABC2DE2 python oncall.py

    --------------------------------------------------------------------------------
    The on call winner is: John Doe
    --------------------------------------------------------------------------------
    
