from app.parsers.base import DocumentParser
from app.parsers.schema import ParsedDocument,ParsedPage


class TXTPARSER(DocumentParser):
    
    def parser(self, file_path:str,) -> ParsedDocument:

        with open(
            file_path,
            encoding="utf-8",
        ) as file:
            
            text = file.read()

            return ParsedDocument(
                pages = [
                    ParsedPage(
                        page_number = 1,
                        text = text,
                    )
                ]
            )
