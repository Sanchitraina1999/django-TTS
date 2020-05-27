# django-TTS
Covert your Text into Speech!

# TTS

So, here is a quick guide for installation of this whole project on your PC and host it locally!

### 1) Clone the Project

clone the project by command:
	
	git clone https://github.com/Sanchitraina1999/django-TTS

after clone you will find the a directory naming textUtils where you cloned this project.

	cd django-TTS

### 2) creating virtual env and installing required packages

install python3-env and pip for creating a envirnoment.

	sudo apt-get install python3-venv python3-pip

create a virtual envirnoment:

	python3 -m venv env

activate this envirnoment:

	source env/bin/activate

installing all required packages which are present in requirements.txt:

	pip3 install -r requirements.txt
	

You are almost Done! ;)

### 3) Running the code

Run this game by command:

	python3 TTS/manage.py runserver
