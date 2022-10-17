from __future__ import print_function

import os

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 
            'https://www.googleapis.com/auth/calendar.events']

CLIENT_FILE = 'client-secret.json'

SPREADSHEET_ID = '1uL1vMhN3Hk6VnNFtV1hPowxoUCRGFDr_GDIUrJ8MqHE' #input('Spreadsheet ID ')
RANGE = 'Menu!C2:D15' #input('Cell Range Ex. Menu!A1:Z1')
NAME = input('Name ')
DAY = input('Day of Takedown(s) ')
TITLE = input('Event Name ')

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    
    try:
        service = build('sheets', 'v4', credentials=creds)
        service1 = build('calendar', 'v3', credentials=creds)

        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range=RANGE).execute()
        values = result.get('values', [])
        if not values:
            print('No Data Found.')
            return

        for row in values:
            for col in row:
                if NAME in col:
                    print(col)
                    event = {
                        'summary': TITLE,
                        'start': {
                            'date': DAY,
                            'timeZone': 'America/Chicago'
                        },
                        'end':{
                            'date': DAY,
                            'timeZone': 'America/Chicago'
                        },
                    }

                    event = service1.events().insert(calendarId='primary', body=event).execute()
                    print('Event created: %s' % (event.get('htmlLink')))
    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()