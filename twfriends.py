import os, time, oauth2, json

try:
    os.mkdir('friends')
except:
    pass

consumer = oauth2.Consumer(key=os.environ['CONSUMER_KEY'], secret=os.environ['CONSUMER_SECRET'])
token = oauth2.Token(key=os.environ['ACCESS_KEY'], secret=os.environ['ACCESS_SECRET'])

def req(url):
    client = oauth2.Client(consumer, token)
    (response, content) = client.request(url)
    return json.loads(content)

account = req('https://api.twitter.com/1.1/account/verify_credentials.json')
friends = req('https://api.twitter.com/1.1/friends/ids.json?user_id=%s' % account['id'])
friendids = friends['ids']
for chunk in (friendids[i:i+100] for i in xrange(0, len(friendids), 100)):
    ids = ','.join(str(s) for s in chunk)
    profiles = req('https://api.twitter.com/1.1/users/lookup.json?user_id=%s' % ids)
    for profile in profiles:
        friendname = profile['screen_name']
        f = open('friends/' + friendname + '.txt', 'w')
        f.write(json.dumps(profile))
        f.close()
        print friendname
    time.sleep(((15*60)/900.0) * 1.5)
