
def handle_event(shoes, day, weather):
    try:
        print('hello')
        if shoes == 'sneakers':
            raise
        print('goodbye')  # Without this, missing branch
    except Exception as e:
        print(e)
        if day == 'Tuesday':
            print('Hamburgers?')
            if weather == 'Sunny':
                print('Oh, boy!')
            # print('wtf')  # Without this, missing branch
        else:
            print('Pizza')

# def simple_event(day, weather):
#     print('did some stuff...')

#     try:
#         if weather == 'Cloudy':
#             raise  
#         # print('wtf')  # without this, missing branch
#     except Exception as e:
#         if day == 'Sunday':
#             print(e)