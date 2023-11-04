import pyshorteners

url = input('Enter the url: ')


def shortenurl(url):
    s = pyshorteners.Shortener()
    print("shortened url-\n",s.tinyurl.short(url))

shortenurl(url)