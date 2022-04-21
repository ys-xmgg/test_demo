from ddt import ddt, file_data

from keyword_ddt.keywords.web_ui import WebDemo
import unittest

@ddt
class CaseDemo(unittest.TestCase):
    @file_data('../data/test_data.yaml')
    # def test_1(self):
    #     wu = WebDemo('Chrome')
    #     wu.open("http://www.baidu.com")
    #     wu.input_txt('id', 'kw', 'aa')
    #     wu.click('id', "su")
        
    # def test_2(self):
    #     wu = WebDemo('Firefox')
    #     wu.open("http://www.baidu.com")
    #     wu.input_txt('id', 'kw', 'bb')
    #     wu.click('id', "su")
    def test_1(self, **kwargs):
        # print(*args)
        print(kwargs)
        # wu = WebDemo('Chrome')
        # wu.open()
        # wu.input_txt('id', 'kw', kwargs['txt'])
        # wu.click('id', "su")

if __name__ == '__main__':
    unittest.main()
    
    