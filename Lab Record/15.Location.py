def get_loc(city):
    loc = [("new york", (40.71385, -73.99191)), ("paris", (48.8575, 2.3514)), ("LA", (34.0549, 118.2426))]
    for name, coordinates in loc:
        if name.lower() == city.lower():
            return coordinates
    return None


city = input("name:")
coordinates = get_loc(city)

if coordinates:
    print(f"{city} is located in {coordinates}")
else:
    print(f"{city} not found")