import fitz

from app.parsers.base import DocumentParser
from app.parsers.schema import ParsedDocument, ParsedPage


class PDFParser(DocumentParser):

    def parse(self, file_path:str) -> ParsedDocument:

        document = fitz.open(file_path)

        pages = []

        for page_number,page in enumerate(document):

            pages.append(
                ParsedPage(
                    page_number=page_number + 1,
                    text =page.get_text()
                )
            )
        
        document.close()

        return ParsedDocument(
            pages=pages,
        )
