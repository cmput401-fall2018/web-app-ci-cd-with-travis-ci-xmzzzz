import unittest
from unittest.mock import patch, mock_open
from unittest import TestCase, mock
from service import Service
#from examples.count_lines.file_reader import FileReader


class Test_service(TestCase):
    
    
    def test_bad_random(self):
        file_content_mock1 = """10\n12\n14\n16\n18\n20\n30"""
        #fake_file_path = 'file/path/mock'
        newfile = mock_open(read_data=file_content_mock1)
        with patch('service.open',newfile,create=True) :
            number1 = Service.bad_random()
    
        expected = len(file_content_mock1.split('\n'))
        assert 0 <= number1 < expected

        
        
    def test_divide(self):
        s = Service()
        s.bad_random = mock.Mock(return_value=10)
        r_val = s.divide(5)
        assert r_val == 2
        
        s.bad_random = mock.Mock(return_value=1)
        #r_val2 = s.divide(0)
        self.assertRaises(ZeroDivisionError,s.divide,0)
        
        '''s.bad_random = mock.Mock(return_value=None)
        r_val3 = s.divide(10)
        assert (TypeError,services.divide(0))'''

        
    
    def test_abs_plus(self):
        s = Service()
        #s.bad_random = mock.Mock(return_value=10)
        r_val = s.abs_plus(-100)
        assert r_val == 101
        
        r_val1 = s.abs_plus(1e-9)
        assert r_val1 == 1e-9+1
        
        
    
    def test_complicated_function(self):
        s = Service()
        s.bad_random = mock.Mock(return_value=10)
        #s.divide = mock.Mock(return_value=2)
        r_val = s.complicated_function(5)
        assert r_val == (2,0)
        
        self.assertRaises(ZeroDivisionError,s.complicated_function,0)
        
    
        
