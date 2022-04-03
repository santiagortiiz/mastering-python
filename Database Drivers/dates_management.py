from datetime import datetime

def add_created_at(object):
    now = datetime.now()
    date_time_string = now.strftime("%d/%m/%Y %H:%M:%S")
    object['created_at'] = date_time_string
