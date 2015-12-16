from temp_conversion import fahr_to_kelvin
from nose.tools import *

def test_basic_value():
	assert fahr_to_kelvin(20.00)==266.4833333333333
	
@raises(TypeError)
def test_temp_string():
	assert fahr_to_kelvin("SomeTemperature")

@raises(TypeError)
def test_null_temp():
	assert fahr_to_kelvin()
	


