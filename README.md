# pfch_final
Miranda Siler | Pratt Institute | Programming for Cultural Heritage | Fall 2020

This project will allow you to create a timeline of roosters at the Brooklyn Museum using KnightLab's TimelineJS program. The project contains three main python files in order to run: get_objects.py, parse.py, and sheets.py. It will require you to get your own Brooklyn Museum and Google API keys, as well as set up a Google Sheet using the template from KnightLab. More details are provided below, as well as an explanation of files that were ignored in this repository.

### get_objects
This file will retrieve object data using the Brooklyn Museum API and download them as separate JSON files.

Before you begin, you will need to [retrieve an API key from the Brooklyn Museum](https://www.brooklynmuseum.org/opencollection/api/register) and save it in a file called passwords.json. You will also need to create a folder called /data.

### parse
This file will parse the data from your separate files according to the information needed from KnightLab's TimelineJS. The result will be a single JSON  file with the cleaned data.

### sheets
This file will take your cleaned data and write it out to a Google Sheet using the pygsheets module, Google Sheets API, and Google Drive API.

Before you begin, you will need to follow all of the [pygsheets module documentation outlined](https://github.com/nithinmurali/pygsheets), retrieving OAuth credentials. This should result in a client_secret.json file, as well as another file that is created once your script has run.

You will also need to set up your Google Sheet. [Download the template from KnightLab](https://timeline.knightlab.com/#make) and save the sheet key in passwords.json. Delete the stock template data, and add the title slide info manually (row 2).

## Acknowledgments
Shout outs go to Matt Miller for teaching this course, Ben Averill for the rooster idea, [chipiatt](https://github.com/chpiatt/brooklyn-museum-mediachain/blob/master/object.py) for helping me understand how to use the Brooklyn Museum API with python, and [nithinmurali](https://github.com/nithinmurali/pygsheets) for the pygsheets module and documentation.
