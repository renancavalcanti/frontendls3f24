from distutils.log import debug

bind = "0.0.0.0:8000"
workers = 1

accesslog = "-"
errorlog = "-"

loglevel = "info"
timeout = 300

"""
gunicorn --worker-tmp-dir /dev/shm TaskManager.wsgi

"""