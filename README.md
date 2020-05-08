# Osquerier_Pygeon
A Web Front-End for Remote, User-Friendly Ad-Hoc Querying Using the Osquery Endpoint Visibility Tool

  These instructions are designed to allow an interested user to install and start experimenting with Osquerier Pygeon locally on Linux, though these instructions should would for most modern Unix-based operating systems. Because Osquerier Pygeon does not yet implement some basic security features that should be standard for a service that by design bears endpoint device details to those that can access it, Osquerier Pygeon in its present state should not be used under any circumstances in any production environment whatsoever.
	In order to install and start experimenting with Osquerier Pygeon, you should first ensure that you have the following software installed, along with any of its required dependencies. Links to the official installation instructions for each are included as hyperlinks:
    • Python 3 (version 3.6+ recommended)
    • Django (version 3.0 recommended)
    • Osquery (version 4.3.0 recommended)
    • Osquery-python (version 3.0.6 recommended)
	Once these dependencies have been installed, clone or download Osquerier Pygeon from its GitHub repository, https://github.com/CaptainB-Team/Osquerier_Pygeon. Once downloaded, run the following commands from the directory created when Osquerier Pygeon was cloned or downloaded, in order, to properly configure Osquerier Pygeon’s internal SQLite database used to store query history and for any administrator account credentials (which can be configured as per the official Django instructions accessible here).

  “manage.py make migrations”
  “manage.py migrate”

	With the above steps completed, you should now be ready to run Osquerier Pygeon. In order to start Osquerier Pygeon, complete the following two (2) steps:
    1. Ensure that your local instance of osqueryd is currently running.
    2. From the directory into which Osquerier Pygeon was cloned or downloaded, run the command “sudo manage.py runserver”.
	With that, Osquerier Pygeon should be up and running. Open your web browser of preference and access the client (located at “localhost:8000/” by default).
