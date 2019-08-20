import codecs

rot13 = codecs.getencoder('rot13')


def dont_google(a, conceal=False):
    'Prevent search engines from indexing a string.'

    if conceal:
        a = a.encode('punycode').decode('us-ascii')
        a = rot13(a)[0]
    else:
        a = rot13(a)[0]
        a = a.encode('us-ascii').decode('punycode')

    return a
