from django.core.files.uploadhandler import TemporaryFileUploadHandler


class CustomFileUploadHandler(TemporaryFileUploadHandler):
    def validate_file_extension(self):
        pass
