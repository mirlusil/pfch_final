import json
import glob

#full dictionary that will be dumped into a json file at end
clean_data = {}

#opening BKM json files
for file in glob.glob('data/*.json'):
    with open(file, 'r') as open_file:
        object = json.load(open_file)

        #parse data
        if object['data']['primary_image'] != None:
            id = object['data']['id']
            if object['data']['object_date_begin'] != None:
                year = object['data']['object_date_begin']
            else:
                #only one case where this happens so entering manually
                year = -332
            month = None
            day = None
            time = None
            if object['data']['object_date_end'] != None:
                end_year = object['data']['object_date_end']
            else:
                #only one case where this happens so entering manually
                end_year = -30
            end_month = None
            end_day = None
            end_time = None
            if object['data']['object_date'] != None:
                display_date = object['data']['object_date']
            else:
                #only one case where this happens so entering manually
                display_date = object['data']['period']
            headline = object['data']['title']
            text = object['data']['description']
            media = object['data']['images'][0]['standard_size_url']
            media_credit = None
            media_caption = object['data']['images'][0]['caption']
            media_thumbnail = object['data']['images'][0]['thumbnail_url']
            type = None
            group = None
            background = None

            #creating list that matches Knightlab specs
            clean_object = [year, month, day, time, end_year, end_month, end_day, end_time, display_date, headline, text, f"https://{media}", media_credit, media_caption, f"https://{media_thumbnail}", type, group, background]

            #update python dictionary
            clean_data.update({id:clean_object})

        else:
            print(f"Skipped {object['data']['id']}, no pictures.")

#dump completed dictionary to json file
with open(f'data/clean_data.json', 'w') as out:
    json.dump(clean_data, out, indent=2)
