import listener
import sql


def handle(evt_type, payload):
    # TODO: insert into DB
    print("FOO")
    print(evt_type, payload)

listener.event_loop(handle)
