import logging
#create logger and file Handler
logger=logging.getLogger('file_logger')
file_handler=logging.FileHandler('application.log')

#Set log lven and formatter
file_handler.setLevel(logging.WARNING)
formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(message)s')
file_handler.setFormatter(formatter)

#Add Handler to loggerr
logger.addHandler(file_handler)

#Log message
logger.warning('This is a warning message')
logger.error("this is an error message")