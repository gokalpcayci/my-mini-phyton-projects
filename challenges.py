travel_log = [
    {"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visited": 12}},
    {"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visited": 15}}
]


def add_new_country(country, total_traveled_day, cities):
    travel_log.append({f"{country}": {"cities_visited": cities, "total_visited": total_traveled_day}})


add_new_country("Turkey", 10, ["Ankara, İstanbul, İzmir"])

for country in travel_log:
    print(country)
