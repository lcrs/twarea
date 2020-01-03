# twarea
Simulate your twitter area (the follow graph as springs)

![twarea screenshot](https://github.com/lcrs/twarea/raw/master/twareascreen.png)

Some output:

[https://vimeo.com/382658114](https://vimeo.com/382658114)

[https://vimeo.com/382677254](https://vimeo.com/382658114)

[https://vimeo.com/382682447](https://vimeo.com/382658114)

The code is "fun!", "exploratory", "casual"

* Hit [https://developer.twitter.com](https://developer.twitter.com), make an app, grab the four keys and set them as the env vars `CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET`
* `twfriends.py` downloads your friends' profiles to json in the friends/ folder
* `twarea.py` downloads you friends' friends' profiles, which takes 8-10 hours because of twitter's API limits
* `twavis.py` downloads everyone's profile pictures
* `twbanners.py` gets their banner pictures
*  the `.hipnc` Houdini scenes build the graph from the json, simulate and render it
