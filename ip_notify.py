import urllib2
import sys
from bs4 import BeautifulSoup

# Web site to pull ip from 
pull_site = urllib2.urlopen("http://ipecho.net").read()
ipadress = ""

# Pulls the current IP adress from the "pull_site" and returns it as a string
def get_ip():
    # Parse the site
    soup = BeautifulSoup(pull_site)
    # Get the html as a string
    html_code = str(soup)
    # Calculate the start of the IP adress
    start_index = 15 + html_code.find("<h1>")
    # Calculate the end of the IP adress
    end_index = html_code.find("</h1>")
    # Return the ip adress from the html
    return html_code[start_index:end_index]

  

