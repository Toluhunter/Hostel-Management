wsgi_app = 'hostel_management.wsgi:application'
accesslog = errorlog = "/var/log/gunicorn/gunicorn.log"

capture_output = True

bind = "0.0.0.0:8000"
workers = 2