import codecs

rot13 = codecs.getencoder('rot13')


def dont_google(a):
    'Prevent search engines from indexing a string.'
    return rot13(a)[0]
