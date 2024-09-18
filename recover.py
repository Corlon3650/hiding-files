# made by Corlon
import pathlib
import shutil
import sys

files_story = pathlib.Path.home() / "unticontr" / "lib" / "files_story.txt"
replace_folder = pathlib.Path.home() / "unticontr" / "lib" / "replaced_files"

if files_story.exists() and replace_folder.exists():
    with files_story.open(mode="r", encoding="utf-8") as story:
        for line in story.readlines():
            renamed_name_file = pathlib.Path(line[:(line.find(";"))])
            base_name_file = pathlib.Path(line[(line.find(";") + 1):line.find("/n")])

            if renamed_name_file.exists():
                renamed_name_file.replace(base_name_file)
            else:
                print(f"The name '{renamed_name_file.name}' isn't found")
                sys.exit()

    with files_story.open(mode="w", encoding="utf-8") as atory: story.close
    shutil.rmtree(replace_folder)
    replace_folder.mkdir(exist_ok=True)
    print("It's ok")

else: print(f"The folder '{replace_folder.name}' or the file '{files_story.name}' isn't found")