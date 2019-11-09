"""lambda_function.py: synch text Alexa skill."""
import json

with open('plainText.json') as data:
    apl_render_directive = json.load(data)


def lambda_handler(event, context):
    """App entry point."""
    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'SSML',
                'ssml': "<speak>Test program.</speak>"
            },
            'shouldEndSession': True,
            'directives': [
                apl_render_directive,
                {
                    "type": "Alexa.Presentation.APL.ExecuteCommands",
                    "token": "scrollToken",
                    "commands": [{
                        "type": "SpeakItem",
                        "componentId": "declarationTextId"
                    }]
                }
            ]
        }
    }
    return response
