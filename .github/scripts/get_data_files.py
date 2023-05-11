import os
import json
import csv
import google.auth
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_sheet_data(spreadsheet_id, sheet_name):
    try:
        # Get the service account key from the environment variable
        key_data = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        credentials = service_account.Credentials.from_service_account_info(key_data, scopes=scopes)
        service = build('sheets', 'v4', credentials=credentials)
        result = service.spreadsheets().values().get(
            spreadsheetId=spreadsheet_id, range=sheet_name).execute()
        rows = result.get('values', [])
        return rows
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def get_sheet_names(spreadsheet_id):
    try:
        # Get the service account key from the environment variable
        key_data = json.loads(os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'])
        scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']
        credentials = service_account.Credentials.from_service_account_info(key_data, scopes=scopes)
        service = build('sheets', 'v4', credentials=credentials)
        result = service.spreadsheets().get(
            spreadsheetId=spreadsheet_id).execute()
        sheets = result.get('sheets', [])
        sheet_names = [sheet['properties']['title'] for sheet in sheets]
        return sheet_names
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None

def save_csv(sheet_name, data):
    with open(f'{sheet_name}.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)

def main():
    spreadsheet_id = '1ZvYGzp6AlhZhXdck00nGYcAF-NtJ92l4JrHlAIKZt70'

    # Get the list of sheet names
    sheet_names = get_sheet_names(spreadsheet_id)

    # Download each sheet as a CSV
    if sheet_names:
        for sheet_name in sheet_names:
            data = get_sheet_data(spreadsheet_id, sheet_name)
            if data:
                save_csv(sheet_name, data)
                print(f"Downloaded {sheet_name}.csv")

if __name__ == '__main__':
    import os
    import json

    # Open the JSON key file and read its content
    with open('getdatafiles-bba278a2e7b6.json', 'r') as key_file:
        key_data = json.load(key_file)

    # Convert the key data to a JSON string and set it as the environment variable
    os.environ['GOOGLE_SERVICE_ACCOUNT_KEY'] = json.dumps(key_data)

    main()
