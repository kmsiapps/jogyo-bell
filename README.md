# Jogyo-Bell
Call your teaching assistant with just one click

### Requirements
see `requirements.txt`

### Run
Edit `config.py` to match your server address (e.g., 127.0.0.1:5000)
`waitress-serve --listen=127.0.0.1:5000 main:app`

### Usage
open `127.0.0.1:5000` (index page) to see call logs
open `127.0.0.1:5000/bell` (call GUI page), or just GET to `127.0.0.1:5000/call` (api)
