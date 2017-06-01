from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        
        "特殊方法在测试方法执行前运行"
        self.brower = webdriver.Firefox()

    def tearDown(self):
        
        "特殊方法在测试完成之后完才"
        self.brower.quit()

    def test_function(self):

        "测试函数"
        self.brower.get("http://localhost:8000")

        self.assertIn('To-Do',self.brower.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings= 'ignore')
