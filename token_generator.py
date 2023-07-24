import jwt
import datetime

def generate_token():
    exp_time = datetime.datetime.now() + datetime.timedelta(minutes=int(525600))
    payload = { 'app_name':'ErrorHub', 'valid_until': str(exp_time) }
    return jwt.encode(payload, 'EJ6K3HLT9G2FIY7O1QX4', algorithm='HS256')

print(generate_token())