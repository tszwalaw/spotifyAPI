import base64

def encodeMessage(message):
    message = f"{message}".encode()
    b64Message = base64.b64encode(message)
    return b64Message
    
    
    
