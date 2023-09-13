import random
import string

class URLShortener:
    def __init__(self):
        self.url_mapping = {}
        self.short_url_length = 10  

    def generate_short_url(self):
        characters = string.ascii_letters + string.digits
        short_url = ''.join(random.choice(characters) for _ in range(self.short_url_length))
        return short_url

    def shorten_url(self, long_url):
        if long_url in self.url_mapping:
            return self.url_mapping[long_url]

        short_url = self.generate_short_url()
        self.url_mapping[long_url] = short_url
        return short_url

shortener = URLShortener()
long_url = input('Enter URL: ')
short_url = shortener.shorten_url(long_url)

print(f"Shortened URL: {short_url}")