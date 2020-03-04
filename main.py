def start(action):
    import read

    url_scan = 'https://tracker.senabo.site/api/scan/'
    url_register = 'https://tracker.senabo.site/api/register/'

    if action.lower() == 'scan':
        read.read(url_scan)
    elif action.lower() == 'register':
        read.read(url_register)
    else:
        print('Unknown action!')
