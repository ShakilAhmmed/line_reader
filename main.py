from Reader.reader import LineReader

if __name__ == "__main__":
    path = input("Enter Folder Path")
    folder_name = input("Enter Folder Name")
    file_reader = LineReader(path, folder_name)
    print(file_reader.files_view())
    file_reader.line_counts()
