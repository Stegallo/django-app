uv run manage.py makemigrations
uv run manage.py migrate
# https://stackoverflow.com/questions/76985252/pythonanywhere-admin-site-css-is-broken-in-django
uv run manage.py collectstatic
# uv run manage.py createsuperuser
