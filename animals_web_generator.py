import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)


def serialize_animal(animal):
    output_data_of_animals = ""
    animal_name = animal["name"]
    characteristics = animal["characteristics"]
    animal_type = characteristics.get("type")
    animal_diet = characteristics.get("diet")
    first_location = animal.get("locations")[0]
    output_data_of_animals += '<li class="cards__item">\n'
    output_data_of_animals += f'<div class="card__title">{animal_name}</div>\n'
    output_data_of_animals += f'<p class="card__text">\n'
    output_data_of_animals += f'<strong>Diet:</strong> {animal_diet}<br/>\n'
    output_data_of_animals += f'<strong>Location:</strong> {first_location}<br/>\n'
    output_data_of_animals += f'<strong>Type:</strong> {animal_type}<br/>\n'
    output_data_of_animals += '</p>'
    output_data_of_animals += '</li>'
    return output_data_of_animals

def animal_details(animals_data):
    output = ""
    for animal_obj in animals_data:
        output += serialize_animal(animal_obj)
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

def main():
    data_of_animals = load_data('animals_data.json')
    animals_list = animal_details(data_of_animals)
    replace_data_in_html(animals_list)

if __name__ == "__main__":
    main()