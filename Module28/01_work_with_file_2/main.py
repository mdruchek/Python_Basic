from typing import TextIO, Optional
import os


class File:
    """
    Контекст-менеджер записи и чтения файлов
    """
    def __init__(self, file_name: str, mode: str) -> None:
        self.file_name = file_name
        self.mode = mode
        self.file_open = None

    def __enter__(self) -> TextIO:
        if not os.path.isfile(self.file_name) and 'w' not in self.mode:
            self.mode = 'w'
        self.file_open = open(self.file_name, self.mode, encoding='utf8')
        return self.file_open

    def __exit__(self, exc_type, exc_val, exc_tb) -> Optional[bool]:
        self.file_open.close()
        if 'file' in str(exc_type).lower():
            return True


with File('text.txt', 'w') as file:
    file.write('Привет')

with File('text.txt', 'r') as file:
    print(file.read())
