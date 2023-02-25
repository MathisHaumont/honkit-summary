import re
import os

with open("SUMMARY.md", "r") as file:
    content = file.read()
    links = re.findall(r"\[(.*)\]\((.*)\)", content)
    folders_and_files = links

for link in folders_and_files:
    title = link[0]
    path = link[1]
    if "#" in path:
        path = path.split("#")[0]
        with open(path, "a") as f:
            f.write("\n# " + title + " {#" + link[1].split("#")[1] + "}\n")
    elif not os.path.exists(path):
        if "." in path:
            directory = os.path.dirname(path)
            if not os.path.exists(directory):
                os.makedirs(directory)
            with open(path, "w") as f:
                f.write("# " + title + "\n")
        else:
            os.makedirs(path)