import os, json, urllib, time

for friend in os.listdir('friends'):
	if not os.path.isdir('friends/' + friend):
		continue
	for theirfriend in os.listdir('friends/' + friend):
		f = open('friends/' + friend + '/' + theirfriend)
		profile = json.load(f)
		url = profile['profile_image_url']
		url = url.replace('_normal.', '.')
		filename = 'avis/' + url.replace('/', '-').replace(':', '-')
		try:
			urllib.urlretrieve(url, filename)
		except:
			print "[%s] Exception: %s // %s // %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e, theirfriend)
			sleep(1)
			continue
