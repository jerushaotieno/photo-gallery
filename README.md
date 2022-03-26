### Author

Jerusha Otieno

### Description

This is a personal gallery application built with Django to display photos for others to see.

### User Story

A user of the application is able to:

* View different photos of interest
* Click on a single photo to expand it and also view the details of the photo. The photo details appear on a modal within the same route as the main page
* Search for different categories of photos (e.g. law, health, business, etc.)
* Copy a link to the photo to share with friends
* View photos based on the location they were taken.

### Getting Started

To get a copy of the project up and running on your local machine for development and testing purposes, clone this repository into a virtual environment and install the package manager, pip. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Install all project requirements using the package manager pip.

(virtual) $ pip install -r requirements.txt

### Installation

Use the .env.example file to create a .env file with appropriate values to get a development env running.

### Running Tests

To run automated tests for the system:

(virtual) $ python3 manage.py test photos 

### Deployment

With all environment variables changed to suit your local copy of this repository, deploy the application to Heroku to see it live or simply run it locally

(virtual) $ python3 manage.py runserver

### Technology Used 

Django 3.0.8 - The web framework used
Heroku - Deployment platform
Python3 - Backend logic
Postresql - Database system

### Known Bugs

There are no known bugs currently but pull requests are allowed incase you spot a bug

### Contact Information

If you have any question or contributions, please email: jerushaotienocoding@gmail.com

### License 

MIT License

### Copyright

Copyright (c) 2022 Jerusha Otieno
