# My manual Y.Metrika class for python

## Python class to work with Y.Metrika API (demo counter presented)

api.request() method inits GET request without token confiramtion (should be added in init section)

traffic() method requests metrics and dimensions relative to visits grouped by date not considering pagination by default, full=True to get all the data considering pagination
