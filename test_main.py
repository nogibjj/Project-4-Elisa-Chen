#adding tests
from get_requests import get_activity

def test_requests():
    activity = get_activity()
    #making sure we're receiving activities
    assert activity['activity']
