import os
    
if os.path.isfile('keys.py'):
    from keys import ConsumerKey, ConsumerSecret, AccessToken, AccessTokenSecret
    os.environ['ConsumerKey'] = ConsumerKey
    os.environ['ConsumerSecret'] = ConsumerSecret
    os.environ['AccessToken'] = AccessToken
    os.environ['AccessTokenSecret'] = AccessTokenSecret