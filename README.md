Housing web scrapper

Libraries Used:
'requests' to extract the HTML data from a website.
'BeautifulSoup' used for parsing the extracted HTML data.
'dateTime' used to return the current time of the user.

The following will be scraped from the website "Realtor.com" (Tags from inspecting the element)
1. Address -> "card-address-1" + "card-address-2"
2. Bath Count -> "property-meta-baths"
3. Bed Count -> "property-meta-beds"
4. SQFT (Square feet) -> "property-meta-sqft"
5. Pricing -> "price-wrapper"

Properties are stored in the class: BasePropertyCard_propertyCardWrap__Z5y4p
Inside a 'div' tag

A text file is created and written to the 'Housing_Data' directory, a text file displaying the results will populate the folder.

Data is displayed in the text file in the following format: 
(1, {'Pricing': '$315,000', 'Bed': '3bed', 'Bath': '2bath', 'Sqft': '1,266sqft1,266 square feet', 'Address': '1770 Castleton Dr Troy, MI 48083'})

  
