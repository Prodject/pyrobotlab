#
# Voices can be found here : http://www.acapela-group.com/?lang=en
# 
#  As of 2016-12-14 the AcapelaSpeech service no longer works.
#  Two alternatives exists.
#  1. Switch to MarySpeech. It's Open source, local and configureble
#  2. Use NaturalReaderSpeech. Same voices as AcapelaSpeech but will fail sooner or later. Uses
#     an internet service that can change at any moment.
#
speech = Runtime.createAndStart("Speech","AcapelaSpeech")
speech.setVoice("Sharon")
speech.speakBlocking("Hello world")
speech.speakBlocking("My name is Sharon")
speech.speakBlocking("I speak English")
speech.speakBlocking("#LAUGH02#")
speech.setVoice("Ines")
speech.speakBlocking(u"Hola Mundo")
speech.speakBlocking(u"mi nombre es Ines")
speech.speakBlocking(u"Hablo español")
speech.speakBlocking("#LAUGH02#")
speech.setVoice("Kal")
speech.speakBlocking(u"Hej världen")
speech.speakBlocking(u"Jag heter Kal")
speech.speakBlocking(u"Jag pratar svenska och kommer från Göteborg")
speech.speakBlocking("#LAUGH02#")
speech.setVoice("Manon")
speech.speakBlocking(u"Bonjour le monde")
speech.speakBlocking(u"Mon nom est Manon")
speech.speakBlocking(u"Je parle français")
speech.speakBlocking("#LAUGH02#")