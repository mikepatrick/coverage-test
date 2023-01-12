from sut import handle_event, simple_event

def test_handle_event():
    handle_event('boots', 'Monday', 'Sunny')
    handle_event('sneakers', 'Tuesday', 'Cloudy')
    handle_event('sneakers', 'Tuesday', 'Sunny')
    handle_event('sneakers', 'Wednesday', 'Cloudy')

def test_simple_event():
    simple_event('Thursday', 'Cloudy')
    # simple_event('Thursday', 'Sunny')  # running this gets rid of 22->exit missing branch
    simple_event('Sunday', 'Cloudy')