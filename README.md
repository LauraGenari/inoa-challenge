# INOA Challenge
This repository is a project for the INOA's hiring avaliation. It is a plataform in which the user add tickers from Yahoo Finance plataform, and set lower and upper tunnels for that asset that triggers a notification email if the value of the action is above the upper tunnel or below the lower tunnel. Also, the user sets the periodicity of checking.

## Requirements
- python3
- pip3

## Installing
1. Create a virtual environment
2. run ``pip install -r requirements.txt``

## Start by
1. Activate your virtual environment
2. run ``python manage.py makemigrations``
3. run ``python manage.py migrate``
4. update .env to real credentials. Suggest using gmail, and here is a short guide:
    1. Enable two-factor authentication on your Google account:
       1. Go to My Google Account and turn on two-step verification (2FA).
    2. Create an app password:
        1. After enabling two-step verification, go to the App Passwords Page.
        2. Select "Other (custom name)" from the drop-down list.
        3. Give the application a name, such as "Django Email", and click "Generate".
        4. You will see a 16 character password that you will use in the EMAIL_HOST_PASSWORD.

## Running the project
Open two terminals and run:
- ``python manage.py runserver``
- ``python run_crons``

> Note that the automated email sending might get really annoying if you set a lower/upper tunnel too far from the average and a short time for checking. It will cause a lot of spam emails.

### And the styling?
Used bootstrap downloaded package to keep it clean and simple :blush:

**Hope you guys liked it**

![cute cat gif](https://media1.tenor.com/m/r1KDajSj-wsAAAAC/thanks-cat.gif)