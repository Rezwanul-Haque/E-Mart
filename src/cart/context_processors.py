"""Things that has to be displayed in all pages, we
can build a context processor to include the current value in the
request context, regardless of the view that processes the request.
"""
from .cart import Cart

def cart(request): ## Add this function to the settings templates context processors under options 
    return {'cart': Cart(request)}
