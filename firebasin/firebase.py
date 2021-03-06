from dataref import RootDataRef
import urlparse

def Firebase(firebaseUrl, ssl_options=None):
    '''Construct a new Firebase reference from a full Firebase URL.'''

    url = urlparse.urlparse(firebaseUrl)
    root = RootDataRef('https://' + url.netloc, ssl_options=ssl_options)
    if url.path == '/' or url.path == '': 
        return root 
    else:
        return root.child(url.path[1:])