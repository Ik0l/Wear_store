# -*- coding:utf-8 -*-

from django.core.files.uploadhandler import FileUploadHandler


class ImageHandler(FileUploadHandler):  # Потом сделать переименование
    def new_file(self, field_name, file_name, content_type, content_length, charset=None):
        pass