import os, json, urllib, time

try:
    os.mkdir('avis')
except:
    pass

for friend in os.listdir('friends'):
    if not os.path.isdir('friends/' + friend):
        continue
    for theirfriend in os.listdir('friends/' + friend):
        f = open('friends/' + friend + '/' + theirfriend)
        try:
            profile = json.load(f)
        except Exception as e:
            print "[%s] Exception: %s // %s // %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e, friend + '/' + theirfriend)
            time.sleep(1)
            continue
        url = profile['profile_image_url']
        url = url.replace('_normal.', '.')
        filename = 'avis/' + url.replace('/', '-').replace(':', '-')
        if(os.path.exists(filename)):
            print 'already got ' + theirfriend
            continue
        try:
            urllib.urlretrieve(url, filename)
        except Exception as e:
            print "[%s] Exception: %s // %s // %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e, theirfriend)
            time.sleep(1)
            continue
