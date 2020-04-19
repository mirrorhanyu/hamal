import glob
from typing import List

from google.google_drive_helper import create_folder_inside, upload


class GoogleApplicationService:

    @staticmethod
    def upload_to_google_drive(
            parent_folder_ids: List[str],
            local_file_path: str,
            file_name: str,
            description: str = ''
    ):
        folder = create_folder_inside(parent_folder_ids, file_name)
        for file in glob.glob(f'{local_file_path}/*'):
            upload(file, [folder.get('id')], description)
