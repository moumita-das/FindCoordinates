# FindCoordinates
A Django project to enable users upload an excel workbook with addresses in the first column, and latitudes and longitudes of the entered addresses are appended to the next columns by making using Google GeoCoding API.

## Getting Started

### Prerequisites
1) Clone or download this repository to your computer. Open your command prompt and navigate to the folder Find_Coords.
2) Get the API key for the project (refer to https://developers.google.com/maps/documentation/geocoding/get-api-key). Please note, billing needs to be enabled for GeoCoding APIs.
3) Paste the API key in the first line of Find_Coords\findCoords\mainpage\google-api-key.txt

### Installing

1) Install Python3 (refer https://realpython.com/installing-python/)
2) Install pip (refer https://pip.pypa.io/en/stable/installing/)
3) Install virtualenv
```
pip install virtualenv
```

Once the initial setup is completed, create a virtual environment and once done, activate it.
```
virtualenv venv
venv\Script\activate
```

4) Install dependencies.
```
pip install requirements.txt
```

## Deploying in localhost

Navigate to findCoords.
```
cd findCoords
```
Run the server and open up http://127.0.0.1:8000/ in web-browser.
```
python manage.py runserver
```
