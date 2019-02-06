from seleniumbase import BaseCase


class BaseTestCase(BaseCase):

    def setUp(self):
        super(BaseTestCase, self).setUp()
        # Add custom setUp code AFTER the super() line

    def tearDown(self):
        # Add custom code BEFORE the super() line
        super(BaseTestCase, self).tearDown()

    def login(self):
        # <<< Placeholder. Add your code here. >>>
        pass

    def example_method(self):
        # <<< Placeholder. Add your code here. >>>
        pass
