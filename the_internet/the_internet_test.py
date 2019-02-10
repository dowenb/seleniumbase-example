from seleniumbase import BaseCase
from the_internet_objects import BasicAuth, BrokenImages, CheckBoxes

class MyTestClass(BaseCase):

    def isChecked(self, checkBox):
        try:
            self.get_attribute(checkBox, 'checked')
            return True
        except:
            return False

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
    
    def test_checkboxes(self):
        self.open(CheckBoxes.url)
        #checkbox1 should default unchecked, and a click should leave it checked
        self.assert_false(self.isChecked(CheckBoxes.checkbox1), 'Checkbox1 should be unchecked')
        self.click(CheckBoxes.checkbox1)
        self.assert_true(self.isChecked(CheckBoxes.checkbox1), 'Checkbox1 should be unchecked')
         #checkbox2 should default checked, and a click should leave it unchecked
        self.assert_true(self.isChecked(CheckBoxes.checkbox2), 'Checkbox2 should be checked')
        self.click(CheckBoxes.checkbox2)
        self.assert_false(self.isChecked(CheckBoxes.checkbox2), 'Checkbox2 should be unchcked')