# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a dictionary in a dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nestin a dictionary in a list
travel_log = [
    {
    "country": "France",
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
    },
    {
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
    },
]
