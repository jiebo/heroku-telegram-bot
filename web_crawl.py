import urllib
import requests

for n in range(386, 387):
    with open('icons/' + str(n) + '.jpg', 'wb') as handle:
        response = requests.get("https://pkmref.com/images/set_1/" + str(n) + ".png", stream=True)

        if not response.ok:
            print response

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)