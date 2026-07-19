from pathlib import Path

from app.storage.base import StrorageProvider


class LocalStorage(StrorageProvider):

    BASE_PATH = Path("uploads")

    async def save(self,filename, content) -> str:
        

        self.BASE_PATH.mkdir(
            exist_ok=True
        )

        path = self.BASE_PATH / filename

        path.write_bytes(content)

        return str(path)