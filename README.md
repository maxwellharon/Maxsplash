# Maxsplash-V2.0
## Maxwell Haron
#### Maxsplash is a personal gallery whereby one can display images which can be seen by other people who log on to the site.Maxsplash is unique because it uses realtime and displays photos that have been uploaded on that particular day.One can also view photos that have been posted on other days.
#### The live link to the Maxsplash is :
 15th July 2018 10.18.44
#### By **Maxwell Haron**
## Installation Requirements
* A web browser
* A virtual environment
* Django
* Internet connection
* Terminal if you want to access the app locally through your computer

####
#### Installation
* Clone,download or fork the the app from this link https://github.com/maxwellharon/Maxsplash
* Install a virtual environment in your project folder by running the following commands `$sudo apt-get install python3.6-venv` and `$ python3.6 -m venv virtual`.To activate the virtual environment run `$ source virtual/bin/activate`
* To install Django,run the following command `$ source virtual/bin/activate` then `pip install django==1.11`
* To confirm whether Django is installed run the python shell by opening the terminal in the project folder and run `python3.6` then `>>> import django` then `>>> django.get_version()`.If Django is present you should get `'1.11.5'`...Congratulations,you now have Django :-)
* To install requirements,go to your shell and enter the command `pip install -r requirements.txt`
* In the terminal,run the app by running the following command `python3 manage.py runserver`
* Go to your browser and open the link http://127.0.0.1:5000 or http:///localhost:5000**
* Enjoy the App :-)...

### Important packages used in app development.

```
dj-database-url==0.5.0
Django==1.11
django-bootstrap3==10.0.1
Pillow==5.2.0
psycopg2==2.7.5
python-decouple==3.1
pytz==2018.5


```

## Categories

+ The pitches are categorized as punchline, product, intrview and promotion pitches.
+ The user can view all these categories whether authenticated or not.

## Maxsplash Specifications.

+ Pictures posted are displayed from the most recent.
+ The user can see the description of a certain picture
+ The user sees the details of the picture e.g Location         posted,category and a short description
+ The user can also view pictures posted on other days

## Known Bugs and Development
* If you run the application in any version of python lower than 3.5.6 you will experiece errors...Alot of them
## Technologies Used
* python3
* Django
* Jinja
* HTML
* Bootstrap
* css


## Support and contact details
If you have any queries regarding the Maxsplash site,Please feel free to contact #Team Maxsplash through maxwellharon54@gmail.com and we will be happy to look into your query

## License
MIT (c) 2018
