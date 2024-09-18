# made by Corlon
import pathlib
import random

def make_name(simbols, x):  # makes file name
    name = "a"
    for m in range(random.randint(4, 7)):
        name += random.choice(simbols)
    name += f"({x}).jpg"
    return name

list_of_formats = ("*.txt", "*.doc", "*.docx", "*.pdf")
simbols_for_name = ("l", "j", "t", "e", "p", "s", "_")
x = 0

base_folder = pathlib.Path.home() / "Desktop"  # the folder from which the files are being replaced
replace_folder = pathlib.Path.home() / "unticontr" / "lib" / "replaced_files"  # the folder where the files will be replaced
files_story = pathlib.Path.home() / "unticontr" / "lib" / "files_story.txt"  # the file where the files pathes will be saved
replace_folder.parent.mkdir(exist_ok=True, parents=True)
replace_folder.mkdir(exist_ok=True)

if base_folder.exists() and replace_folder.exists():
    for i in list_of_formats:
        files = list(base_folder.rglob(i))  # creates the list of files with a specific format

        for n in files:
            if n.exists():

                  # creates fake files
                if random.randint(1, 50) < 45:
                    for y in range(random.randint(1, 3)):
                        full_new_name = make_name(simbols_for_name, x)
                        full_new_name = full_new_name[0:2] + random.choice(tuple("mn")) + full_new_name[3: ]
                        fake_file = replace_folder / full_new_name
                        fake_file.touch(exist_ok=True)
                        x += 1
                full_new_name = make_name(simbols_for_name, x)
                replace_file = replace_folder / full_new_name

                  # saves the file path
                with files_story.open(mode="a", encoding="utf-8") as story:
                    story.write(f"{replace_file};{n}\n")

                n.replace(replace_file)  # replaces the file
                x += 1
            else:
                print(f"The file '{n.name}' isn't found")
    print("It's ok")
else: print(f"The folder '{base_folder}' or the folder '{replace_folder.name}' isn't found")