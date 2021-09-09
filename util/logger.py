import logging

def getLogger(loggerPath, debugLevel=logging.DEBUG):
    if loggerPath is None:
        return None
    
    logger = logging.getLogger(loggerPath)
    logger.setLevel(debugLevel)
    
    streamHandler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    streamHandler.setFormatter(formatter)
    logger.addHandler(streamHandler)
    

    return logger
