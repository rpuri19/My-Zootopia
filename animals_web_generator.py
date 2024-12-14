import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
number_of_records = len(animals_data)
def animal_details():
    for animal in animals_data:
        animal_name = animal["name"]
        characteristics = animal["characteristics"]
        animal_type = characteristics.get("type")
        animal_diet = characteristics.get("diet")
        first_location = animal.get("locations")[0]
        print (f"Name: {animal_name}")
        print (f"Type: {animal_type}")
        print (f"First Location: {first_location}")
        print (f"Diet: {animal_diet}")
        print("--------")
animal_details()