import webbrowser

latitude = 16.816263
longitude = 96.191315

# Create a Google Maps URL
google_maps_url = f"https://www.google.com/maps?q={latitude},{longitude}"

# print("Open this URL in your browser:", google_maps_url)

webbrowser.open(google_maps_url)
print(f"take a look at your browser to get the location of {latitude}, {longitude}")
