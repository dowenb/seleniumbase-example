from seleniumbase import BaseCase
from the_internet_objects import BasicAuth, BrokenImages

class MyTestClass(BaseCase):

    def test_basic_auth(self):
        self.open(BasicAuth.url)
        self.assert_text(
            'Congratulations! You must have the proper credentials.',
            BasicAuth.success_text
            )
    
    def test_broken_images(self):
        self.open(BrokenImages.url)
        self.assertGreater(int(self.get_attribute(BrokenImages.image1, 'naturalWidth')), 0)
        self.assertGreater(int(self.get_attribute(BrokenImages.image2, 'naturalWidth')), 0)
        self.assertGreater(int(self.get_attribute(BrokenImages.image3, 'naturalWidth')), 0)