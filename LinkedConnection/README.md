# Linked Connections
 
Connections Viewer Backend(Python3 and Django) and Frontend (React)

## Backend Server
Step 1: Install Django
Step 2: python manage.py runserver

## Frontend Server
Step 1: npm install
Step 2: npm run start

## API's
* Initialize Connections
* Description: Initialize dummy data
* URL: "/initialize/"
* METHOD: GET
* Params:
  1. numUsers: number

* Get All Connections
* Description: Fetch all connections in a paginated manner
* URL: "/connections/"
* METHOD: GET
* Params:
  1. page: number
  2. pageSize: number


* Fetch User Connections
* Description: Get all the connections of user associated with userId
* URL: "/userConnections/"
* METHOD: GET
* Params:
  1. userId: number

* Fetch Connections 
* Description: Get connections based on name and locations
* URL: "/connectionByNameLocation/"
* METHOD: GET
* Params (either one param is mandatory):
  1. name: string
  2. location: string


# Steps to run application:
Step 1: Run Backend Server
Step 2: Run Frontend Server
Step 3: Click on Fetch All Button on the Databoard

