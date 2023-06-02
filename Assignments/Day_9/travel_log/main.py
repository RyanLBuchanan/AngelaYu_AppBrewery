# Create an initial list of dictionaries representing travel log entries
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

# Function to add a new country entry to the travel log
def add_new_country(country, visits, cities):
    # Create a new dictionary for the new country
    new_country_dictionary = {}

    # Assign values to the keys of the new country dictionary
    new_country_dictionary["country"] = country
    new_country_dictionary["visits"] = visits
    new_country_dictionary["cities"] = cities

    # Append the new country dictionary to the travel log
    travel_log.append(new_country_dictionary)

# Add a new country entry using the function
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

# Print the updated travel log
print(travel_log)
