import time
import urllib2
import sys
from bs4 import BeautifulSoup

# Web site to pull IP from 
pull_site = urllib2.urlopen("http://ipecho.net").read()
ip_adress = ""

# Pulls the current IP address from the "pull_site" and returns it as a string
def get_ip():
    # Parse the site
    soup = BeautifulSoup(pull_site)
    # Get the html as a string
    html_code = str(soup)
    # Calculate the start of the IP address
    start_index = 15 + html_code.find("<h1>")
    # Calculate the end of the IP address
    end_index = html_code.find("</h1>")
    # Return the IP address from the html
    return html_code[start_index:end_index]

# Emails the specified user with the new IP address
def notify():
    # for testing
    print ip_adress


# Loop forever, checking for change occasionally
while True:
    current_ip_adress = get_ip()
    if ip_adress == current_ip_adress:
        # IP has not changed, sleep
        time.sleep(900)
    else:
        # Update the IP address 
        ip_adress = current_ip_adress
        # Notify the user of the change
        notify()

