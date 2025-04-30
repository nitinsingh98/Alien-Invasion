from project import set_caption,get_clock,is_running,not_running

def test_set_caption():
    assert set_caption('caption') == None

def test_is_running():
    assert is_running() == True

def test_not_running():
    assert not_running() == False
