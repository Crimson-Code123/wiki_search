import requests
import json

# https://googlechromelabs.github.io/chrome-for-testing/known-good-versions-with-downloads.json
URL = "https://en.wikipedia.org/w/rest.php/v1/search/title?q={0}&limit={1}"
URL2 = "https://en.wikipedia.org/w/index.php?limit={0}&fulltext=1&ns0=1&profile=advanced&search={1}" #0; page limit; 1; search text
UA = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:143.0) Gecko/20100101 Firefox/143.0"}
SEARCHES = {}

def gettext(query, limit):
	text = requests.get(headers=UA, url=URL.format(query, limit), timeout=15).text
	obj = json.loads(text)
	return obj

def load():
	global SEARCHES
	with open("saved.txt", "r") as f:
		l = f.readlines()


def store():
	with open("saved.txt", "+w") as f:
		pass

def main():
	global SEARCHES
	while True:
		i = input()
		js = gettext(i, 100)
		for x in js["pages"]:
			f = x["key"]
			r = x["title"]
			s = x["description"]
			SEARCHES[f] = s
			print("{0} -> {1}".format(r, s))
		# store()

if __name__ == "__main__":
	main()

