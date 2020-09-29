# TujipimeHIV
# install and start virtual environment
pip3 install -r requirements.txt
# run migrations
python3 manage.py makemigrations
python3 manage.py migrate

# create admin to login and enter data
python3 manage.py createsuperuser

# Run for job scheduling
python3 manage.py crontab add
# Start server 
python3 manage.py runserver