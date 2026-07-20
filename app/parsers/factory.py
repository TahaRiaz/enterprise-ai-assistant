from app.parsers.pdf_parser import PDFParser
from app.parsers.txt_parser import TXTPARSER
from app.core.exceptions import AppException


class ParserFactory:

    @staticmethod
    def create(
        self,
        content_type:str,
    ):
        if content_type == "application/pdf":
            return PDFParser()
        elif content_type == "text/plain":
            return TXTPARSER()
        else:
            raise AppException(
                "Unsupported document type",
            )