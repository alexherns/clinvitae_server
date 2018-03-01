import os

def get_connection():
    try:
        if os.environ['CLINVITAE_ENV'] == 'production':
            # connect to a real database, except that hasn't been implemented
            raise Exception('Production database interface not implemented')
        else:
            # assume we're using a mock db
            db_path = os.environ['CLINVITAE_DB']
            from dev import connect

            return connect(db_path)
    except:
        raise Exception('Environment undefined! Specify CLINVITAE_ENV and CLINVITAE_DB')
