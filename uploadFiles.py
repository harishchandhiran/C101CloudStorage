#I have problems with creating access token in my laptop.
#The rest of the code is good.
#Apart from the access token Everything works fine.The code to use the access token is also correct
#Importing dropbox module
import dropbox

#Creating a class TransferData which will initilize access token and opening the file to be moved
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = ''
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    file_to = input("enter the full path to upload to dropbox:- ")

    transferData.upload_file(file_from, file_to)
    print("file is moved")

main()