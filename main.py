# Essential Libraries that will be used:

# Request used to extract the HTML data from the website.
import requests

# Beautiful soup used for parsing the extracted HTML data.
from bs4 import BeautifulSoup

# To get date and time of results
from datetime import datetime
timeResult = datetime.now().strftime("\nDate: %m-%d-%Y  Time: %H:%M:%S\n")
print(timeResult)

# The following will be scraped from the website "Realtor.com" (Tags from inspecting the element)
# 1. Address
# 2. Bath Count -> "property-meta-baths"
# 3. Bed Count -> "property-meta-beds"
# 4. SQFT (Square feet) -> "property-meta-sqft"
# 5. Pricing -> "price-wrapper"

# Properties are stored in the class: BasePropertyCard_propertyCardWrap__Z5y4p
# Inside a 'div' tag

# Extracting the HTML data --------------------------------------------------------------------------------------------

def get_Houses(location, price):

    # Two variables to store the data

    store_list = list()
    obj = {}

    # Simulate a human visitor, so we initialize the header with User Agent, which will be passed with a GET request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    }

    # By using "Requests" make an HTTP connection on the target URL
    base_url = "https://www.realtor.com/realestateandhomes-search/"
    search_url = f"{base_url}{location}/type-single-family-home/price-{price}"

    res = requests.get(search_url, headers=headers).text

    # BeautifulSoup will navigate through the HTML and obtain the required information
    soup = BeautifulSoup(res, 'html.parser')

    # Select() method allows us tp capture all the elements with the class "BasePropertyCard_propertyCardWrap__Z5y4p"
    for element in soup.select(".BasePropertyCard_propertyCardWrap__Z5y4p"):
        # Get the class the pricing property is contained in and div tag
        try:
            obj["Pricing"] = element.select_one(".price-wrapper div[data-testid=card-price]").text
        except:
            obj["Pricing"] = None

        # Getting bed, bath, and SQFT information from the HTML page. (Extracting data points) -------------------------
        # Using a try and except in case an error occurs or if a category is missing
        try:
            obj["Bed"] = element.select_one("li[data-testid=property-meta-beds]").text
        except:
            obj["Bed"] = None
        try:
            obj["Bath"] = element.select_one("li[data-testid=property-meta-baths]").text
        except:
            obj["Bath"] = None
        try:
            obj["Sqft"] = element.select_one("li[data-testid=property-meta-sqft]").text
        except:
            obj["Sqft"] = None

        # Getting Address
        try:
            obj["Address"] = element.select_one("div[data-testid=card-address-1]").text + " " + element.select_one("div[data-testid=card-address-2]").text
        except:
            obj["Address"] = None

        # Append the objects into the "store_list" array to store each property data.
        store_list.append(obj)
        obj = {}
    #print(store_list)

    print(f"\nReturning Results for {location} with a price range of {price}\n")
    if store_list:
        for item in enumerate(store_list, start=1):
            print(f"{item}\n")
        # Write results to external text file, generating unique file based on time and date
        current_time = datetime.now().strftime("%m-%d-%Y__%H-%M-%S")
        f = open(f"Housing_Data/{current_time}", "w")
        f.write(f"Results for {location}\n")
        for item in enumerate(store_list, start=1):
            f.write(f"{item}\n")
        print(f"Content added to {f}")


loc = input("Enter a location (Example City-Name_State): ")
pri = input("Enter a price range (Min-Max): ")
get_Houses(loc, pri)





