import requests

def get_color_name(rgb):
    url = f"http://www.thecolorapi.com/id?rgb={rgb[0]},{rgb[1]},{rgb[2]}"
    response = requests.get(url)
    data = response.json()
    return data['name']['value']

def color_name(color_tuples):
    color_names = []

    for rgb_values in color_tuples:
        try:
            # Call your color classification function here and get the color name
            color_name = get_color_name(rgb_values)

            # Append the color name to the list
            color_names.append(color_name)
        except Exception as e:
            # Handle errors if needed
            print(f"Error processing RGB values {rgb_values}: {e}")

    return color_names