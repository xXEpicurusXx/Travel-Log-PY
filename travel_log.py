travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

    #this looked complicated but it wasnt, each key needed to be added to a new dictionary that we called new_country{}
    #we created new keys in the dicrtionary.
    #then we linked thaose keys to the position in the function
    #once this new dictionary was created, we appended the travel log by addign the new_country{} dictionary to the travel log

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#when we called this function it added a new dictionary using that function then appended that dictionary inside the travel log with the 
#information associated with its position in the functino call. 


print ("\n".join([str(x) for x in travel_log])) # then we printed it ion a way that was readable becasue i hate the way a dictionary prints 
