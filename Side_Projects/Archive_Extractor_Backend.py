import zipfile

def extract_archive(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive("C:\\Users\\MY PC\\Desktop\\python_projects\\daily_journal\\compressed.zip",
                    "C:\\Users\\MY PC\\Desktop\\python_projects\\daily_journal")
