# basic-alexa-text-synch
simple code to demonstrate and test Alexa APL for speech/text synchronization

Amazon documentation for this feature is located at https://developer.amazon.com/docs/alexa-presentation-language/apl-speech-and-text-synchronization-for-text-blocks.html

Code is written in Python, located in [src/](src/) folder
included are json files which contain the `Alexa.Presentation.APL.RenderDocument` used by the lambda_handler.

This separation allows experimentation with different `RenderDocument`s.  Here are their descriptions:

* [plainText.json](src/plainText.json) - most basic implementation taking a single text ("declarationSsml") and transforming it to "speech" via the `ssmlToSpeech` and "text" via the "ssmlToText" transformer.  I would expect this to be read in a synchronized fashion, but when executed it first scrolls through the entire text on the screen, then reads it all.
