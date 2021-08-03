# Zendesk Coding Challenge 2021
A web application using flask protocol for viewing ticket details from the Zendesk API.

## Requirements
- Python 3.7
- Flask
- venv
- User name and Token to access the Zendesk API. Generate the OAth token following this link https://support.zendesk.com/hc/en-us/articles/203663836-Using-OAuth-authentication-with-your-application

## Installing
### Unix/Mac
Redirect to the downloaded project folder. Run the commands in terminal.

`python3 -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

## Running

`cd zendesk/src`


`python main.py`


Once the flask framework running successfully. Please copy the link http://127.0.0.1:5000/ to your local browser to view and interact with this application

## Testing
After complete the Intsalling step

`cd zendesk/tests`

`python unit_test.py`

This program will run the unit testing for the request functions used in the program.



