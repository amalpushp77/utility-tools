from pdf2image import convert_from_path
from pathlib import Path


class P2IConverter:
    def __init__(self, source, destination="converted"):
        self.file_type = {".pdf"}
        self.source = Path(source)
        self.destination = Path(destination) if destination != "converted" else self.source/Path(destination)

        if self.source.is_dir():
            self.__from_path(self.source)
        elif self.source.is_file():
            self.__from_file(self.source)
        else:
            raise Exception("Not sure what source path refer")

    def __from_path(self, source):
        for file in list(source.glob('**/*')):
            if file.suffix in self.file_type:
                out = self.destination / file.stem
                if not out.exists():
                    out.mkdir(parents=True, exist_ok=True)

                convert_from_path(file, fmt="jpg", poppler_path="./poppler-22.04.0/Library/bin",
                                  output_folder=out,
                                  output_file="")

    def __from_file(self, source):
        out = self.destination / source.stem
        if not out.exists():
            out.mkdir(parents=True, exist_ok=True)

        convert_from_path(source, fmt="jpg", poppler_path="./poppler-22.04.0/Library/bin",
                          output_folder=out,
                          output_file="")
