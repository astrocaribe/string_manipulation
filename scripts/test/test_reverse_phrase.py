from .. import reverse_phrase
import pytest

from sys import version_info

# Test suite
# ------------------------------------------------------------------------

# pytest fixtures
def setup_module(module):
    pass
    # print ("setup_module      module:%s" % module.__name__)

def teardown_module(module):
    pass
    # print ("teardown_module   module:%s" % module.__name__)

def setup_function(function):
    pass
    # print ("setup_function    function:%s" % function.__name__)

def teardown_function(function):
    pass
    # print ("teardown_function function:%s" % function.__name__)


# Default python version is assumed to be 2
def test_python3_version():
    assert reverse_phrase.is_python3( version_info[0] ) == False

# Force version to be 3
def test_python2_version():
    version = 3

    assert reverse_phrase.is_python3( version ) == True

# Test phrase reversal
def test_reverse_the_phrase():
    input_phrase = 'foo bar'

    reversed_phrase = reverse_phrase.reverse_the_phrase( input_phrase )

    assert reversed_phrase == 'bar foo'

# Test reverse_word
def test_reverse_word():
    input_word = 'foo'

    reverse_word = reverse_phrase.reverse_the_phrase( input_word )

    assert reverse_word != 'oof'

def test_main():
    pass
