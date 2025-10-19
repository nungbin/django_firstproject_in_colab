# Installation Guide (learning from this [youtube](https://youtu.be/0roB7wZMLqI?si=4pS1F9CYk2xuM_oN))

## Run the below steps in the terminal of colab
1. Perform a git pull. ```git clone https://github.com/nungbin/django_firstproject_in_colab.git```
2. In the terminal, type in ```pip install django``` to install Django.

## Preparation of running the app. Run the below steps in the terminal
3. npm install --global http-server
4. npm install -g ngrok
5. npm install -g concurrently

## Install and start PostgreSQL. Run the below steps in the terminal
6. apt install postgresql postgresql-contrib &>log
7. service postgresql start

## At this point, the database should be up and running
### Run the highlighted steps in the terminal
8. ```sudo -i -u postgres```
9. ```psql```: run the client
10. ```\c postgres```:connect to the database
11. ```\password postgres```: change the password for the user postgres. Jot down the username and password for DATABASE section in SETTINGS.PY

## Run the below steps in the terminal to create/adjust table(s) in the database
12. python manage.py makemigrations
13. python manage.py migrate

## Create an ngrok Account ([credit](https://github.com/MohamedEmad300/Hosting-Web-Apps-on-Colab?tab=readme-ov-file))
Visit the [ngrok](https://ngrok.com/) website and sign up for a free account.
Once registered, log in to your ngrok dashboard.
Locate your authentication token in the dashboard under the "Setup & Installation" section.
Copy the token to your clipboard for use in the Colab notebook.
### Run the below steps in the terminal
14. ngrok config add-authtoken "```<authentication token>```"
15. curl ipv4.icanhazip.com
16. cd /content/firstproject
17. concurrently "python manage.py runserver 8501" "ngrok http 8501 --log=stdout"

## To test with two URLs
* (url generated from step 10)
* (url generated from step 10)/app/function
### set up super user credentials
* ```python manage.py createsuperuser```
* (url generated from step 10)/admin
