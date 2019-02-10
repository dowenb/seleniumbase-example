def _url(path, prefix='http://'):
    base_url = 'the-internet.herokuapp.com'
    return prefix + base_url + path
    # TODO get base URL from some sort of environment variable that can be set via CI


class BasicAuth(object):
    url = _url('/basic_auth', prefix='http://admin:admin@')
    success_text = '#content > div > p'


class BrokenImages(object):
    url = _url('/broken_images')
    image1 = '#content > div > img:nth-child(2)'
    image2 = '#content > div > img:nth-child(3)'
    image3 = '#content > div > img:nth-child(4)'


class CheckBoxes(object):
    url = _url('/checkboxes')
    checkbox1 = '#checkboxes > input[type="checkbox"]:nth-child(1)'
    checkbox2 = '#checkboxes > input[type="checkbox"]:nth-child(3)'