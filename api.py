import requests
###IMDB
'''url = "https://imdb236.p.rapidapi.com/imdb/tt7631058/cast"

headers = {
	"x-rapidapi-key": "daa363154dmshe76d0afe7645585p173c89jsn28f8a435ae2d",
	"x-rapidapi-host": "imdb236.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
print(response)  #Status of the response
data = response.json()

if isinstance(data,list):
    print("Response is a list")
    for i in data:
        print(i["fullName"])
elif isinstance(data,dict):
    print(data)
    '''

###YH finance

'''url = "https://yahoo-finance15.p.rapidapi.com/api/v1/markets/stock/quotes"

querystring = {"ticker":"AAPL,MSFT,^SPX,^NYA,GAZP.ME,SIBN.ME,GEECEE.NS"}

headers = {
	"x-rapidapi-key": "daa363154dmshe76d0afe7645585p173c89jsn28f8a435ae2d",
	"x-rapidapi-host": "yahoo-finance15.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json() '''

###Jobs

'''url = "https://linkedin-api8.p.rapidapi.com/search-jobs-v2"

querystring = {"keywords":"golang","locationId":"92000000","datePosted":"anyTime","sort":"mostRelevant"}

headers = {
	"x-rapidapi-key": "daa363154dmshe76d0afe7645585p173c89jsn28f8a435ae2d",
	"x-rapidapi-host": "linkedin-api8.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
a = data.get("data")
print("Total Data:\n")
print(data)
print("**********************")
print(f"Jobs available{a}")
print("************************************************")
print(type(a))
for i in a:
    print({i["location"]})'''

###IRCTC
'''url = "https://irctc1.p.rapidapi.com/api/v1/getTrainScheduleV2"

querystring = {"trainNo":"12936"}

headers = {
	"x-rapidapi-key": "daa363154dmshe76d0afe7645585p173c89jsn28f8a435ae2d",
	"x-rapidapi-host": "irctc1.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
data = response.json()
print(data)
a = data.get("data")
print(a)

print("**********************************************") '''


### RTO VEHICLE
'''import requests

url = "https://rto-vehicle-details.p.rapidapi.com/%7BregNo%7D"

headers = {
	"x-rapidapi-key": "daa363154dmshe76d0afe7645585p173c89jsn28f8a435ae2d",
	"x-rapidapi-host": "rto-vehicle-details.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())'''



