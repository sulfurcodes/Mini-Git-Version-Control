import json
from pathlib import Path

class Repository:
    def __init__(self, path = '.'):
        self.path = Path(path).resolve()
        self.git_dir = self.path / '.mini-git'
        self.objects_dir = self.git_dir / 'objects'
        self.refs_dir = self.git_dir / 'refs'
        self.heads_dir = self.refs_dir / 'heads'
        self.head_file = self.git_dir / 'head'
        self.index_file = self.git_dir / 'index'

    def init(self) -> bool:
        if self.git_dir.exists():
            return False   
        
        self.git_dir.mkdir()
        self.objects_dir.mkdir()
        self.refs_dir.mkdir()
        self.heads_dir.mkdir()

        self.head_file.write_text('ref: refs/heads/master\n')
        self.index_file.write_text(json.dumps({}, indent=2))

        print(f'Inititalized an empty Git repository in {self.git_dir}')
        return True

    def add_file(self, path: str):
        full_path = self.path / path

        if not full_path.exists():
            raise FileNotFoundError(f'Path {path} not found')

        content = full_path.read_bytes()
         

    def add_path(self, path: str) -> None:
        full_path = self.path / path

        if not full_path.exists():
            raise FileNotFoundError(f'Path {path} not found')
        if full_path.is_file():
            self.add_file(path)
        if full_path.is_dir():
            self.add_directory(path)