import dropbox
class TransferData :
    def __init__ (self, access_token):
        self.access_token=access_token

    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        F= open(file_from, "rb")
        dbx.files_upload(F.read(),file_to)

def main():
    access_token = "sl.AqC32WVILnV0QRD9YbEZOS0ZIlw88tYF8PHTgRn9RE6aLFzE_FxAzRDY6vASxkpMrL3aRT8RK0xofjlyJSkpD5SS2WFwRR_WKLTg6qp6m80JoliTU7dJlcKMNOLPstQ3WkJhOig"
    transferData = TransferData(access_token)   
    file_from = input("Enter the File to Tranfer Data")
    file_to = input("Enter the Full Path to upload to Dropbox")
    transferData.upload_files(file_from,file_to)
    
    print("File Has Been Moved")
main()    
