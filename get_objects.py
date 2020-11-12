import json
import requests

#Thanks to https://github.com/chpiatt/brooklyn-museum-mediachain/blob/master/object.py for helping me realize that the api key should go in headers not payload
passwords = json.load(open('passwords.json'))
headers =  {'api_key' : passwords['bkm_key']}

base_url = 'https://www.brooklynmuseum.org/api/v2/object/'
payload = {
    'keyword' : 'rooster',
    'has_images' : 1,
    'limit' : 25,
    'offset' : 0
}

#previous work told me that there are 48 results that meet my criteria
#getting relevant results
counter = 0
while counter < 48:
    r = requests.get(base_url, headers=headers, params=payload)

    objects = json.loads(r.text)
    objects = objects['data']

    #downloading single objects as separate json files
    for single_object in objects:
        obj_id = single_object['id']
        obj_r = requests.get(f'https://www.brooklynmuseum.org/api/v2/object/{obj_id}', headers=headers)

        try:
            obj_data = json.loads(obj_r.text)
            with open(f'data/{obj_id}.json', 'w') as out:
                json.dump(obj_data, out, indent=2)
        except:
            print(f'something went wrong with {obj_id}')

        counter += 1

    #getting rest of the results
    payload['offset'] += 25
