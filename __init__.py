import os

def where():
    f = os.path.split(__file__)[0]

    return os.path.join(f, 'ca_certs.pem')
