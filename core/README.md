
<h1 align='center'>REST API FOR NEWS APP </h1>
<br>
News server with authozation on python, using Django and Django RestFramework.

<h2 align='center'>Installing<h2>
	
1 - clone project
<br>
2 - register on https://newsapi.org/register and get your own API-KEY
<br>
3 - open `newsblog/news/views.py` direction and save your KEY in API_KEY constant.

## How to get up and running
Once you've cloned the project and have got your api-key, navigate to the root directory of the project in cmd. Run the following commands from this directory:

1. ` docker-compose up -d `

The docker-compose command will build the images from dockerfile and docker-compose.yml file. This will create ports, links between containers, and configure applications as requrired. 

2. ` docker-compose run web_run `
At first you need sign in - `http://0.0.0.0:8000/register` and after press `go to the home page` wich ll redicrect you to the `http://0.0.0.0:8000/news/`(this ll collect some data in database).
*You can also delete all data from database by follow `http://0.0.0.0:8000/deletenews/`.

# API DOCUMENTATION

## Avalible API methods for blog posts:

GET - /api/listnews/ - Retrieve All News
GET, POST - /api/createuser/ - Retrieve All Users And Allow Register New One
GET - /api/auth/id/ - Allow To Get Token By Provide User's ID
<br>
	
