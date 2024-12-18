import blpapi
from blpapi import SessionOptions, Session

def start_bloomberg_session():
    """
    Start and authenticate Bloomberg API session.
    """
    session_options = SessionOptions()
    session_options.setServerHost("localhost")
    session_options.setServerPort(8194)

    session = Session(session_options)
    if not session.start():
        raise ConnectionError("Failed to start Bloomberg API session.")
    print("Bloomberg API session started.")

    if not session.openService("//blp/refdata"):
        raise ConnectionError("Failed to open Bloomberg Reference Data service.")
    print("Reference Data service opened.")
    return session

if __name__ == "__main__":
    try:
        session = start_bloomberg_session()
        print("Bloomberg API is ready.")
    except Exception as e:
        print(f"Error: {e}")
