# CodeAlpha_urlshortner
In the given code, the input function is used to take the url from the user as input. This input url is then passed to the shortenurl function.

Inside the shortenurl function, a new Shortener object is created from the pyshorteners module. The shortener object has a tinyurl attribute which can be used to shorten the url.

The short method of the tinyurl attribute is called with the url passed as an argument. This method returns the shortened url.

Finally, the shortened url is printed out to the console.
