Django REST Framework 

Application - Restaurant visit diary

How to run: 

1. Download or clone this repository: 
git clone https://github.com/LevytskyiS/DRF.git

2. Install and activate a virtual environment: 
python -m venv venv
./venv/Scripts/activate

3. Run 'pip install -r rvd/requirements.txt'

4. Go to the projet folder (rvd), create a .env file and define the following variables 
(for docker compose keep HOST as 'localhost', also keep the HOST=postgres line commented, we will change it in the next steps): 

SECRET_KEY=
ENGINE=django.db.backends.postgresql
NAME=
USER=
PASSWORD=
HOST=localhost
#HOST=postgres
PORT=5432

5. Run 'docker compose up -d'
6. Run 'python manage.py migrate'
7. Create superuser 'python manage.py createsuperuser'
8. Run 'docker compose stop'
9. Uncomment the 'web' service in docker-compose.yml
10. Change HOST=localhost to HOST=postgres, so there will be a bridge between django application and postgres
11. Run 'docker compose up -d'
12. Check Swagger - 'http://127.0.0.1:8000/swagger/ (if you want to try it out, you should use Postman or Django login, cause the access token is not recognized for some reason by Swagger)
13. The application is launched on server already and you can also check the swagger and other API urls under the link below: 
http://207.154.244.142:8001/swagger/ 