# import code for encoding urls and generating md5 hashes
import urllib
import hashlib


def get_avatar(email, size=80):
    # Set your variables here
    default = "https://www.example.com/default.jpg"

    # construct the url
    gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(email.lower()).hexdigest() + "?"
    gravatar_url += urllib.urlencode({'d': default, 's': str(size)})
    return gravatar_url
