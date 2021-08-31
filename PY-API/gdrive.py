from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import os

credentials_dir = 'credentials_module.json'

# LOGIN
def login():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(credentials_dir)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(credentials_dir)
    else:
        gauth.Authorize()

    return GoogleDrive(gauth)

# CREATE A SIMPLE TXT FILE
def create_text_file(file_name, content, folder_id):
    credentials = login()

    # You can remove 'parents' key to save directroy to the root drive
    file = credentials.CreateFile({
        'title': file_name,
        'parents': [{
            'kind': 'drive#fileLink',
            'id': folder_id
        }]        
    })
    file.SetContentString(content)
    file.Upload()

    # To give sharing permissions
    permission = file.InsertPermission({
        'type': 'anyone',
        'role': 'reader'
    })

    # Download URL
    print('webContentLink:', file['webContentLink'])
    # Online View URL
    print('alternateLink:', file['alternateLink'])


# UPLOAD A FILE TO DRIVE
def upload_file(file_path, folder_id):
    credentials = login()

    file_name = file_path.split('/')[-1]

    file = credentials.CreateFile({
        'title': file_name,
        'parents': [{
            "kind": "drive#fileLink", 
            "id": folder_id
        }]
    })

    # file['title'] = file_path.split("/")[-1]
    file.SetContentFile(file_path)
    file.Upload()

    # Add sharing permisions
    file.InsertPermission({
        'type': 'anyone',
        'role': 'reader'
    })
    # Download URL
    print('webContentLink:', file['webContentLink'])
    # Online View URL
    print('alternateLink:', file['alternateLink'])


# DELETE/RESTORE FILES
def delete_restore(file_id):
    credentials = login()
    file = credentials.CreateFile({'id': file_id})
    # MOVE TO TRASH
    file.Trash()
    # RESTORE FROM TRASH
    file.UnTrash()
    # DELETE PERMANENTLY
    file.Delete()

# CREATE FOLDER
def create_folder(folder_name, folder_id):
    credentials = login()
    folder = credentials.CreateFile({
        'title': folder_name,
        'mimeType': 'application/vnd.google-apps.folder',
        'parents': [{
            "kind": "drive#fileLink",
            "id": folder_id
        }]
    })
    folder.Upload()


if __name__ == "__main__":
    folder_id = '1XFOgO9snFQeKX7unXuoqsEmnGW66gG65'

    # create_text_file('hello', 'Hello World!', folder_id)

    # file_path = os.path.join(os.path.abspath(os.getcwd()), 'wallpaper.jpg')
    # file_path = file_path.replace('\\', '/')
    # upload_file(file_path, folder_id)

    # delete_restore('type your file id')
