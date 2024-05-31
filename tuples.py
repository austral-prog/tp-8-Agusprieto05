def get_coordinate(record):
    treasure, place = record
    return place

print(get_coordinate(("fdfdsafdsafd", "2A")))


def convert_coordinate(coordinate):
    place = coordinate
    return tuple(place)

print(convert_coordinate("2A"))

def create_record(azara_record, rui_record):
    what, position = azara_record
    place, point, colour = rui_record
    position = tuple(position)
    if position == point:
        return what,position,place,point,colour
    else:
        return "No coincidence"
