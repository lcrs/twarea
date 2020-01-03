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
for friendid in friends['ids']:
    try:
        friendname = req('https://api.twitter.com/1.1/users/show.json?user_id=%s' % friendid)['screen_name']
    except KeyError as e:
        # End up here when a friend disappears
        print "[%s] Failed to get name for friend %s, skipping" % (time.strftime("%Y%m%d %H:%M:%S"), friendid)
        continue
    friendfolder = 'friends/%s' % friendname
    try:
        os.makedirs(friendfolder)
    except:
        pass

    try:
        theirfriends = req('https://api.twitter.com/1.1/friends/ids.json?user_id=%s' % friendid)['ids']
        for chunk in (theirfriends[i:i+100] for i in xrange(0, len(theirfriends), 100)):
            ids = ','.join(str(s) for s in chunk)
            profiles = req('https://api.twitter.com/1.1/users/lookup.json?user_id=%s' % ids)
            for profile in profiles:
                theirfriendname = profile['screen_name']
                f = open(friendfolder + '/' + theirfriendname + '.txt', 'w')
                f.write(json.dumps(profile))
                f.close()
                print '%s follows %s' % (friendname, theirfriendname)
            time.sleep(((15*60)/900.0) * 1.5)
        time.sleep(((15*60)/15.0) * 2.5)
    except Exception as e:
        print "[%s] Exception, sleeping 16 minutes: %s // %s // %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e, friendname)
        time.sleep(60*16)
        continue
