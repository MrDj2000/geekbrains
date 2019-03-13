from text.controllers import ( get_lower_text, get_upper_text)


TEST_TEXT = 'SOME_TEXT'
ASSERT_TEXT = 'some_text'

def test_get_lower_text_is_lower():
    assert get_lower_text(TEST_TEXT) == ASSERT_TEXT