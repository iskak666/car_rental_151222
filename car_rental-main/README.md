py -m venv venv
cd venv/Scripts/activate
cd ../..
pip install -r requirements.txt
cd car_rental
python manage.py runserver


http://127.0.0.1:8000/
