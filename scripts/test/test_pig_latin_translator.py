from .. import pig_latin_translator
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

def test_python3_version():
    version = 2

    assert pig_latin_translator.is_python3( version ) == False

def test_python2_version():
    version = 3

    assert pig_latin_translator.is_python3( version ) == True

def test_vowel_rule_applies():
    pig_word = pig_latin_translator.apply_vowel_rule( 'orbituary' )

    assert pig_word == 'orbituaryyay'

def test_vowel_rule_doesnt_apply():
    pig_word = pig_latin_translator.apply_vowel_rule( 'foo' )

    assert pig_word != 'oofay'

def test_consonant_rule_applies():
    pig_word = pig_latin_translator.apply_consonant_rule( 'foo', 1 )

    assert pig_word == 'oofay'

def test_consonant_rule_doesnt_apply():
    pig_word = pig_latin_translator.apply_consonant_rule( 'are', 0 )

    assert pig_word != 'areyay'

def test_vowel_with_punctuation_translation():
    pig_word = pig_latin_translator.apply_vowel_rule( 'orbituary!' )

    assert pig_word == 'orbituaryyay!'

def test_consonant_with_punctuation_translation():
    pig_word = pig_latin_translator.apply_consonant_rule( 'foo!', 1 )

    assert pig_word == 'oofay!'

def test_punctuated_word():
    pig_word, punc = pig_latin_translator.split_punctuation( 'foo!' )

    assert pig_word == 'foo' and punc == '!'

def test_unpunctuated_word():
    pig_word, punc = pig_latin_translator.split_punctuation( 'foo' )

    assert pig_word == 'foo' and punc == ''

def test_main():
    pass
