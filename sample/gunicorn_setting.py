import os

host = "0.0.0.0"
port = os.getenv("PORT", 5000)

bind = str(host) + ":" + str(port)

reload = True
accesslog = "-"
loglevel = "debug"

proc_name = "Infrastructure-Ts"
worker = 3
worker_class = "sync"
