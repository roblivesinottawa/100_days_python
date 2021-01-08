travel_log = [
  {
    "country": "France", 
    "cities": ["Paris", "Lille", "Nice"], 
    "visits": 0
  },
  {
    "country": "Germany", 
    "cities": ["Berlin", "Hamburg"], 
    "visits": 0
  },
]

def add_new_country(country_visited, city_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities"] = city_visited
    new_country["visits"] = times_visited
    travel_log.append(new_country)


add_new_country("Portugal", ["Lisbon"], 0)
add_new_country("Spain", ["Madrid"], 0)
add_new_country("USA", ["New York"], 2)
print(travel_log)
