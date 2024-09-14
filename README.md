# White-Hats

(hardware part) [invloves these file 1BrailleVision.py, 1arduino.code ]
(blind-deaf)

The idea revolves around developing a prototype device that converts visual elements like text and colors from images into Braille, a tactile writing system used by visually impaired individuals.

1. Image Processing: The prototype will first analyze an image to identify text and colors. This involve using Optical Character Recognition (OCR) for text and color detection algorithms.

2. Text Conversion to Braille: The identified text will be translated into Braille characters by python script at backend. This python script is further linked with Arduino code for serial communication. 

3. Color Representation in Braille: Since color is a visual concept, a system will be devised to translate colors into a tactile format. This might involve assigning specific patterns or textures to different colors.

4. Tactile Output: The converted Braille text and color representations will be output through a physical interface that can be touched and felt by deaf-blind users. This is a custom-built surface that can dynamically change to represent different Braille characters and patterns.


   hardware O/P = 1st phase able to made 2*3 matrix, representing letter which is changing 1 by 1 each milli sec through LED.





(Software) [involves these file 2VisionVoice.py, 1quadrant.py]
only for Blind (open cv – tesseract – speaker) 
Surrounding input signals to Speaker (earphone)




(Software) [involves these file 3SignSpeak.py]
only for Dumb (opencv, numpy, mediapipe)
Sign Language to Text Translate to Speaker




(Software) [involves these file 4TextTalk.py]
only for Deaf (opencv, numpy, mediapipe)
Speech to Text Converter for deaf Individuals
