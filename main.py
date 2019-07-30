import requests
import json
import numpy as np

LATITUDE = 33.746026 
LONGITUDE = -84.390658
RADIUS = 32000 # ~20mi radius
NUMSITES = 100   #500

PLOTLY_UN = 'stomy1'
PLOTLY_API_KEY = '2jLklvsASX01PKxb7sLB'
MAPBOX_ACCESS_TOKEN = "pk.eyJ1Ijoic2V0aHRvbXkiLCJhIjoiY2pteHBmeHBmMGJ0dDN3bTl0bDBjOHJhdiJ9.5YY_WBnxgJc3JAAkuuL1wQ"

def get_nearby_sites(lat = LATITUDE, lon = LONGITUDE, radius = RADIUS, numSites = NUMSITES):
    """Get numSites amount of sites w/in radius.
    Keyword arguments:
    radius(String) -- radius of search in meters
    numSites(String) -- how many sites you want returned
    
    Returns:
    Dictionary with list of: store-ids, latitudes, longitudes, site-names
    """
    
    # NCR API Call
    url = "https://gateway-staging.ncrcloud.com/site/sites/find-nearby/33.746026%20,-84.390658"

    querystring = {"radius": radius,"numSites": numSites}  

    headers = {
        'Content-Type': "application/json",
        'nep-application-key': "8a00860b6641a0ae0166471356ba000f",
        'Authorization': "Basic YWNjdDpqYW1AamFtc2VydmljZXVzZXI6MTIzNDU2Nzg=",
        'Cache-Control': "no-cache",
        'Postman-Token': "5130f289-eec6-4ae0-9ba6-f4cd3fefcdb0"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    # load json into lists
    response_dict = json.loads(response.text)
    
    site_dict = {}
    #hours_open_list = []
    #hours_closed_list = []
    for i in range(0, len(response_dict['sites']) - 1):
        site_dict[response_dict['sites'][i]['id']] = [response_dict['sites'][i]['coordinates']['latitude'],
                                                      response_dict['sites'][i]['coordinates']['longitude'],
                                                      response_dict['sites'][i]['siteName']]
            
    return site_dict

a = get_nearby_sites()

print(a)
