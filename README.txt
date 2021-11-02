CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Requirements
 * Installation
 * FAQ
 * Maintainers
 
INTRODUCTION
------------

The MBTA Departure Board displays the current commuter rail departures for
the selected station. When you load the page, select a station from the drop-down
menu and click Submit to populate the table.

 * The source code for this application is located at:
   https://github.com/donnalmartin/mbta_departures_project/

 * To submit bug reports and feature suggestions:
   https://github.com/donnalmartin/mbta_departures_project/issues
   
REQUIREMENTS
------------

This application requires the following modules:

 * [Django](https://github.com/django/django.git)
 * [requests](https://github.com/psf/requests.git)
 
INSTALLATION
------------
 
 * Install as you would normally install a contributed Django project.
 
   - git clone https://github.com/donnalmartin/mbta_departures_project.git

   - py -m venv mbta_departures_project

   - .\mbta_departures_project\Scripts\activate

   - cd mbta_departures_project

   - pip install -r requirements.txt

   - python manage.py migrate

   - ***Enter your SECURITY_KEY settings.py.***

   - python ./manage.py runserver

FAQ
---

Q: For some stations, the page takes several seconds to load. Is this expected?

A: Yes, some stations will take longer to load than others due to the amount of
associated data available. Some lag is normal while the system waits to hear back
from the MBTA API, but performance improvements within this application should be
investigated as well.

Q: The second row of the departures table appears blank. Is this expected?

A: No, you should be seeing the current date and time in this row. This has been
identified as a browser incompatibility issue. For this reason, we recommend using
the latest availble version of your browser.
   
MAINTAINERS
-----------

Current maintainers:
 * Donna Martin (donnalmartin) - https://github.com/donnalmartin
