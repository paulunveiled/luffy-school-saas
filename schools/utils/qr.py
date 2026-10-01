import json
import hmac
import hashlib
from django.conf import settings

def generate_signature(payload_dict):
    payload_str = json.dumps(payload_dict, sort_keys=True)
    secret_key = settings.SECRET_KEY.encode('utf-8')
    
    return hmac.new(
        secret_key, 
        payload_str.encode('utf-8'), 
        hashlib.sha256
    ).hexdigest()

def verify_signature(payload_dict, provided_signature):
    expected_signature = generate_signature(payload_dict)
    return hmac.compare_digest(expected_signature, provided_signature)