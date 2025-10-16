# Installation Guide (learning from this [youtube](https://youtu.be/0roB7wZMLqI?si=4pS1F9CYk2xuM_oN))

1. Under the ```/content```folder. Create a folder ```firstproject```.
2. ```cd firstproject```
3. Run ```git init``` to initialize a repository
4. Perform a git pull. ```git pull git@github.com:nungbin/django_firstproject_in_colab.git```
5. In the terminal, type in ```pip install django``` to install Django.

## Below steps are for the preparation of running the app
4. npm install --global http-server
5. npm install -g ngrok
6. npm install -g concurrently

## Create an ngrok Account ([credit](https://github.com/MohamedEmad300/Hosting-Web-Apps-on-Colab?tab=readme-ov-file))
Visit the [ngrok](https://ngrok.com/) website and sign up for a free account.
Once registered, log in to your ngrok dashboard.
Locate your authentication token in the dashboard under the "Setup & Installation" section.
Copy the token to your clipboard for use in the Colab notebook.

7. ngrok config add-authtoken "```<authentication token>```"
8. curl ipv4.icanhazip.com
9. cd /content/firstproject
10. concurrently "python manage.py runserver 8501" "ngrok http 8501 --log=stdout"

## To test with two URLs
* (url generated from step 10)/app/function
* (url generated from step 10)/app/class
