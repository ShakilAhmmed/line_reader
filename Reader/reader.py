import os


class LineReader:
    def __init__(self, path, file):
        self.path = path.strip()
        self.file = file.strip()

    def folder_files(self):
        main_path = self.path + '/' + self.file
        files = []
        folders = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(main_path):
            for folder in d:
                folders.append(os.path.join(r, folder))
            for file in f:
                if '.' in file:
                    files.append(os.path.join(r, file))

        return files

    def files_view(self):
        for f in self.folder_files():
            print(f)

    def line_counts(self):
        lines = 0

        for f in self.folder_files():
            try:
                with open(f, 'r') as file_pen:
                    lines = lines + len(file_pen.readlines())
            except Exception as e:
                print("Stucked", e)

        print(lines)
