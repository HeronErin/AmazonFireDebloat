import urllib.parse

def YouTubeSearch(query):
	query=urllib.parse.quote_plus(query)
	return f"amzns://apps/android?p=com.amazon.firetv.youtube#Intent;S.intentToFwd=youtube://search?query={query}&isVoice=false&launch=searchinapps;end"

def YouTubeVideo(id):
	return f"amzns://apps/android?p=com.amazon.firetv.youtube#Intent;S.intentToFwd=youtube://youtube.com/watch?v={id};end"
import base64
def KodiUri(uri):
	uri=base64.urlsafe_b64encode(uri.encode("utf-8")).decode("utf-8")
	uri = f"plugin://script.redirect.fav/_B64_/{uri}#Intent;component=org.xbmc.kodi/.Splash;end"
	uri=urllib.parse.quote_plus(uri)
	print(uri)
	return f"amzns://apps/android?p=org.xbmc.kodi#Intent;S.intentToFwd={uri};end"




