import os

if __name__ == "__main__":
    projectName = input("Enter project name: ")
    projectType = input("Static (0) or Dyanmic (1): ")

    defaultProjectLocation = "F:\\"
    npmInit = "npm init -y"

    filePath = os.path.join(defaultProjectLocation, projectName)
    os.mkdir(filePath)
    os.chdir(filePath)

    if int(projectType) == 0:
        try:
            publicFolder = os.path.join(filePath, "public")
            os.mkdir(publicFolder)
            os.chdir(publicFolder)
            with open("index.html", "w") as fp:
                print("Creating projects...")
                try:
                    cssFolder = os.path.join(publicFolder, "css")
                    os.mkdir(cssFolder)
                    os.chdir(cssFolder)
                    with open("index.css", "w") as fp:
                        try:
                            jsFolder = os.path.join(publicFolder, "js")
                            os.mkdir(jsFolder)
                            os.chdir(jsFolder)
                            with open("index.js", "w") as fp:
                                print("Project Created!")
                                os.chdir(publicFolder)
                                os.popen("code .").read()
                        except OSError as e:
                            print(e)
                except OSError as e:
                    print(e)
        except OSError as e:
            print(e)
    elif int(projectType) == 1:
        try:
            with open("server.js", "w") as fp:
                print("Creating Project...")
                publicDir = os.path.join(filePath, "public")
                os.popen("code .").read()

        except OSError as e:
            print(e)
