# Mandrill Events Tracker

## Starting the application

For running mongodb in docker container follow next steps:

1. Install docker engine: https://docs.docker.com/engine/install/
2. Install docker compose: https://docs.docker.com/compose/install/
3. Open a terminal window in project directory and run `docker-compose up` command.

Otherwise make sure mongodb is up and running locally and is available on default port.

To start the application open a new terminal tab and run `uvicorn main:app`

## Testing

To send a batch of events from Mandrill run:
```bash
python3 tests/factories/mandrill_webhook_mock.py
```

To send a single click event go to `http://localhost:8000/events/test` in your browser.
