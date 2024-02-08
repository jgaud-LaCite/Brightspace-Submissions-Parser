import os, patoolib, re, sys, shutil

def unzip_files_in_folder(folder_path):
    # Get a list of all files in the folder
    files = os.listdir(folder_path)
    print(files)
    # Iterate through each file in the folder
    for file in files:
        file_path = os.path.join(folder_path, file)

        # Check if the file is a .zip or .rar file
        if file.endswith('.zip') or file.endswith('.rar'):
            pattern = r'\d+-\d+ - (.+?) -'

            # Search for the name in the input string
            match = re.search(pattern, file)

            # Check if a name match is found
            if match:
                print(f"Unzipping: {file}")
                # Extract the first and last names from the matched groups
                name = match.group(1)
                output_folder = folder_path + "/" + name

            else:
                output_folder = folder_path + "/Unknown_" + file
                
            try:
                patoolib.extract_archive(file_path, outdir=output_folder)

                # Remove the original .zip or .rar file after extraction
                os.remove(file_path)


            except Exception as e:
                print(f"Error extracting {file}: {e}\n")

def move_files_with_ext(folder_path):
    extensions = sys.argv[2:]

    # Move all files with the specified extension to the root directory
    subdirectories = [d for d in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, d))]

    for subdirectory in subdirectories:
        subdirectory_path = os.path.join(folder_path, subdirectory)
        
        for root, _, files in os.walk(subdirectory_path):
            for file in files:
                if any(file.endswith(suffix) for suffix in extensions):
                    # Move the file to the root directory
                    src_path = os.path.join(root, file)
                    dest_path = os.path.join(subdirectory_path, file)

                    # Check if file already exists and change the name if so
                    base, ext = os.path.splitext(dest_path)
                    i = 1
                    while os.path.exists(dest_path):
                        dest_path = f"{base}_{i}{ext}"
                        i += 1
                    
                    shutil.move(src_path, dest_path)
        
        # Remove sub-directories
        directories = [d for d in os.listdir(subdirectory_path) if os.path.isdir(os.path.join(subdirectory_path, d))]
        for directory in directories:
            directory_path = os.path.join(subdirectory_path, directory)
            shutil.rmtree(directory_path)

    

if __name__ == "__main__":
    if not sys.argv[1]:
        print("Please specified a file path")
    else: 
        unzip_files_in_folder(sys.argv[1])
        if sys.argv[2]:
            move_files_with_ext(sys.argv[1])