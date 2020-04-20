import os
from typing import List

from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials
from googleapiclient.http import MediaFileUpload

# https://github.com/googleapis/google-api-python-client/issues/620

SCOPES = [
    'https://www.googleapis.com/auth/drive'
]
credentials = Credentials.from_service_account_file('google-service-account-credential.json', scopes=SCOPES)
service = build('drive', 'v3', credentials=credentials)


def upload(file_name: str, folder_ids: List[str], description: str = ''):
    file_metadata = {
        'name': os.path.basename(file_name),
        'description': description,
        'parents': folder_ids
    }
    media = MediaFileUpload(file_name)
    return service.files().create(body=file_metadata, media_body=media, fields='id').execute()


def create_folder_inside(parent_folder_ids: List[str], sub_folder_name: str):
    file_metadata = {
        'name': sub_folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': parent_folder_ids
    }
    return service.files().create(body=file_metadata, fields='id').execute()

