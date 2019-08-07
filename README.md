# Mozio


Functions
---------------

1. Create, Update, Delete, Lists Provider.
2. Create, Update, Delete, Lists ServiceArea.
3. Search Polygon according to lat and long.

Getting Started

	To work on the test code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

	bitbucket repo :

	git clone

	1)Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

		$ virtualenv -p python3.6 venv

	2)Activate the virtual environment:

		$ source venv/bin/activate

	3)Install Python dependencies for this project:

		$ pip install -r requirements.txt

	4)For Database schema:

		$ python manage.py migrate

	5)Create Super User

		$ python manage.py createsupersuer

	6)Start the Django development server:

		$ python manage.py runserver


Rest APIs
---------------


Step1: CRUD Operations in Providers:
	
	Method : GET, POST
     http://127.0.0.1:8000/provider/

    POST API DATA:
       {
		    "name": "name",
		    "email": "name@gmail.com",
		    "language": "English",
		    "currency": "INR",
		    "phone_number": "1530"
		}

     Expected GET Output:
     {
	    "count": 1,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "url": "http://127.0.0.1:8000/provider/1/",
	            "name": "Jhon wick",
	            "email": "jw@gmail.com",
	            "language": "English",
	            "currency": "USD",
	            "phone_number": "98****1530"
	        }
	    ]
	}

	Method : UPDATE, DELETE
	    DELETE:
           url :http://127.0.0.1:8000/provider/1 # Here 1 is provider id

        UPDATE:
           Url: http://127.0.0.1:8000/provider/1 # Here 1 is provider id
           Data:
	           {
		            "name": "Jhon wick",
		            "email": "jw@gmail.com",
		            "language": "English",
		            "currency": "INR",
		            "phone_number": "98****1530"
		        }


Step2: CRUD Operations in service-area:
	Method : GET, POST
     http://127.0.0.1:8000/service-area/

    POST API Data:
    	{
            "provider": "1",
            "name": "Inside africa",
            "price": 21.0,
            "area": 31,
            "mpoly": "SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481, 22.13676452636719 11.44839617401166, 22.40043640136718 18.6521004771425, 16.28929138183593 20.26026464944022, 18.28536987304687 15.01177978112481)))"
        }

    Expected GET output:
    	{
		    "count": 2,
		    "next": null,
		    "previous": null,
		    "results": [
		        {
		            "url": "http://127.0.0.1:8000/service-area/5/",
		            "provider": "http://127.0.0.1:8000/provider/1/",
		            "name": "Afrika",
		            "price": 222.0,
		            "area": 222,
		            "mpoly": "SRID=4326;MULTIPOLYGON (((4.391784667968747 32.62087018318108, 16.88323974609375 29.34267830248893, 26.80664062499999 29.32591746930778, 34.97222900390624 20.80233659297902, 41.90597534179686 9.260713181867553, 45.63720703125 6.019019363914672, 39.85702514648437 -2.071844477055492, 28.96682739257812 -28.54833838763142, 19.51583862304687 -30.47471581151384, 14.62692260742188 -18.00746792135298, 15.35888671875 -6.581395858207814, 10.74600219726563 7.640220359946578, -9.805297851562491 8.057869896976522, -13.34701538085937 23.54888092385873, -4.827117919921863 33.17778985580033, 4.391784667968747 32.62087018318108)))"
		        },
		        {
		            "url": "http://127.0.0.1:8000/service-area/6/",
		            "provider": "http://127.0.0.1:8000/provider/1/",
		            "name": "Inside africa",
		            "price": 21.0,
		            "area": 31,
		            "mpoly": "SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481, 22.13676452636719 11.44839617401166, 22.40043640136718 18.6521004771425, 16.28929138183593 20.26026464944022, 18.28536987304687 15.01177978112481)))"
		        }
		    ]}

	Method : UPDATE, DELETE
	    DELETE:
           url :http://127.0.0.1:8000/service-area/1 # Here 1 is service-area id

        UPDATE:
           Url: http://127.0.0.1:8000/service-area/1 # Here 1 is provider id
           Data:
	           {
		            "provider": "1",
		            "name": "Inside africa",
		            "price": 21.0,
		            "area": 31,
		            "mpoly": "SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481, 22.13676452636719 11.44839617401166, 22.40043640136718 18.6521004771425, 16.28929138183593 20.26026464944022, 18.28536987304687 15.01177978112481)))"
		        }

Step3: Search Area According to Lat and long:
	Method : GET
	http://127.0.0.1:8000/area/?lat=18.28536987304687&lon=15.01177978112481
    
    OUTPUT:
	    {
	    "count": 2,
	    "next": null,
	    "previous": null,
	    "results": [
	        {
	            "provider": "http://127.0.0.1:8000/provider/1/",
	            "name": "Afrika",
	            "price": 222,
	            "area": 222,
	            "mpoly": "SRID=4326;MULTIPOLYGON (((4.391784667968747 32.62087018318108, 16.88323974609375 29.34267830248893, 26.80664062499999 29.32591746930778, 34.97222900390624 20.80233659297902, 41.90597534179686 9.260713181867553, 45.63720703125 6.019019363914672, 39.85702514648437 -2.071844477055492, 28.96682739257812 -28.54833838763142, 19.51583862304687 -30.47471581151384, 14.62692260742188 -18.00746792135298, 15.35888671875 -6.581395858207814, 10.74600219726563 7.640220359946578, -9.805297851562491 8.057869896976522, -13.34701538085937 23.54888092385873, -4.827117919921863 33.17778985580033, 4.391784667968747 32.62087018318108)))"
	        },
	        {
	            "provider": "http://127.0.0.1:8000/provider/1/",
	            "name": "Inside africa",
	            "price": 21,
	            "area": 31,
	            "mpoly": "SRID=4326;MULTIPOLYGON (((18.28536987304687 15.01177978112481, 22.13676452636719 11.44839617401166, 22.40043640136718 18.6521004771425, 16.28929138183593 20.26026464944022, 18.28536987304687 15.01177978112481)))"
	        }
	    ]} 
