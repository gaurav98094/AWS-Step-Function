import json

def lambda_handler(event, context):
    
    validate = False

    if "name" in event and "phoneno" in event:
        if event["name"] and event["phoneno"]:
            validate = True
        
    return {
        "validate": validate 
    }
