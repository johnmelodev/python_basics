import logging
'''
debug - I'm just providing information for developers
info - I just want to inform something that is happening in the program, but it is not an error
warning - I want to alert about something that is happening, possibly unexpected, but it is not yet an error, but it can generate one in the future.
error - An error occurred in the application
critical - An error with serious consequences has just occurred in the application.
'''

logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='a',
                    format='%(levelname)s - %(message)s')  # set the level


logging.critical('Logging critical level')
logging.debug('Logging at debug level')
logging.info('Logging at info level')
logging.warning('Logging at warning level')
logging.error('Logging at error level')
logging.critical('Logging at critical level')
