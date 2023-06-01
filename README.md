LEE, JARETTE ALBERT I.
IT6 FINAL HANDS ON EXAM

***************************************************************************************
MUST NEED!!!
1.POSTMAN
2.FLASK
3.MYSQL CONFIGURATION
4.JSON
5.PYTHON
6.IDE
****************************************************************************************
HOW TO RUN THE PROGRAM

download postman because that's where we'll check the response of our api,
also make sure the mysql configuration is correct. run the file, if the file was run successfully.
get its http address and paste it in postman.
follow the postman commands to display your desired action.

****************************************************************************************
POSTMAN COMMAND

GET
= http://localhost:5000/favsongs?
format

GET USING SONG_NUMBER
= http://localhost:5000/favsongs/parameter?format

POST
=http://localhost:5000/favsongs

note: body > raw > json
(write your changes in body, set it into a raw and make it a json file)

PUT
= http://localhost:5000/favsongs/song_id

DELETE
= http://localhost:5000/favsongs/song_id