import os, json, urllib, time

for friend in os.listdir('friends'):
	if not os.path.isdir('friends/' + friend):
		continue
	for theirfriend in os.listdir('friends/' + friend):
		f = open('friends/' + friend + '/' + theirfriend)
		profile = json.load(f)
		try:
			url = profile['profile_banner_url']
			filename = 'banners/' + url.replace('/', '-').replace(':', '-') + '.jpg'
			urllib.urlretrieve(url, filename)
		except Exception as e:
			print "[%s] Exception: %s // %s // %s" % (time.strftime("%Y%m%d %H:%M:%S"), type(e), e, theirfriend)
			time.sleep(1)
			continue
