class BasicAuth(object):
    url = 'http://admin:admin@the-internet.herokuapp.com/basic_auth'
    success_text = '#content > div > p'

class BrokenImages(object):
    url = 'http://the-internet.herokuapp.com/broken_images'
    image1 = '#content > div > img:nth-child(2)'
    image2 = '#content > div > img:nth-child(3)'
    image3 = '#content > div > img:nth-child(4)'