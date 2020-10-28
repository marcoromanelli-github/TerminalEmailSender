# TerminalEmailSender
Simple package which implements the functionality of a mail service provider usable as a python package and from CMI.

<div align="center">
    <img src="img/automatic_mail_logo.jpeg" width="300" height=300/>
</div>


This very simple package implements the functionality of a mail service provider usable from a terminal. It is possible to
use this software as it is out of the box. The use must be aware og the SMTP server s/he is going to use. The same holds for
the service port and the password. If this script is launched from an IDE the protection of the passwork is not guaranteed 
and it will be probably showed on the screen. This script has been created using Python 3.4.

The most useful application of these classes is when the user needs to send multiple emails which must have the same style
and formatting and a different content. For instance one could read students' marks and emails from a *.csv* file and send
each student an individual email with a fixed structure and the student's private data content. 

Added more user friendly feedbacks in case exceptions occur.

To execute the main software just type 
```console
foo@bar:~$ python emailSender.py
```
on a terminal (python >= 3.4 required). The program will ask for the needed information.

We added an option --time_delay or -td to add schedule a message delivery after a 
delay interval in seconds (300 seconds in the example below):
```console
foo@bar:~$ python emailSender.py -td 300
```

<sub><sup>The letter envelope template is courtesy of [psdgraphics](https://www.psdgraphics.com/).
