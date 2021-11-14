# Mailsac-Examples
This repository is the documentation for Mailsac. It includes examples, service
information, privacy policy, and terms of services.

## Build Instructions
These documents are published to docs.mailsac.com, they can be built locally
for testing purposes.

1. Clone this repo
   `git clone https://github.com/mailsac/mailsac-examples.git`

2. Change directories to the cloned repo
   `cd mailsac-examples`

3. Setup virtual environment (option but helps isolate python modules)
   `python3 -m venv venv`
   `source venv/bin/activate`

4. Install sphinx
   `pip3 install -r requirements.txt`

5. Run build script
   `make html`

6. Build results can be found in `_build/html/`

7. Optional - run a server to view the html output.
    `npm install http-server -g`
    `http-server _build/html`

8. Alternatively the reStructuredText Visual Studio Code extension can be used for live previews

Copyright © 2019 by Forking Software LLC
