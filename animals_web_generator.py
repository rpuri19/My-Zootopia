import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data('animals_data.json')
number_of_records = len(animals_data)

def animal_details():
    output = ""
    for animal in animals_data:
        animal_name = animal["name"]
        characteristics = animal["characteristics"]
        animal_type = characteristics.get("type")
        animal_diet = characteristics.get("diet")
        first_location = animal.get("locations")[0]
        output += f"Name: {animal_name}\n"
        output += f"Type: {animal_type}\n"
        output += f"First Location: {first_location}\n"
        output += f"Diet: {animal_diet}\n"
        output += f"\n"
    return output

def replace_data_in_html (data):
    # Open the HTML file
    with open('animals_template.html', 'r') as file:
        # Read the file's contents
        html_content = file.read()

    new_output = html_content.replace("__REPLACE_ANIMALS_INFO__", f"{data}")
    print(new_output)

    with open('animals_output.html', 'w') as output_file:
        output_file.write(new_output)

animals_list = animal_details()
replace_data_in_html(animals_list)

