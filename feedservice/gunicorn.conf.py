import multiprocessing
import os

bind = "unix:/tmp/feedparser.sock"
#workers = multiprocessing.cpu_count()
workers = 2

errorlog = "/var/log/gunicorn/feedparser/error.log"
accesslog = "/var/log/gunicorn/feedparser/access.log"
loglevel = "info"
access_log_format = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s %(T)s "%(f)s" "%(a)s"'

