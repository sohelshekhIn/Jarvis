import os

projectName = input("Enter project name: ")
defaultProjectLocation = "F:\\demo"
virtualEnv = "py -m virtualenv -p py venv"
activateVenv = "venv\\Scripts\\activate"
projectType = input("Project(0) or site(1): ")
installFlask = "pip install flask"


if int(projectType) == 0:
    try:
        filePath = os.path.join(defaultProjectLocation, projectName)
        os.mkdir(filePath)
        os.chdir(filePath)
        with open("index.py", "w") as fp:
            print("Creating Project...")
            try:
                os.popen("pip install virtualenv").read()
                os.popen(virtualEnv).read()
                os.popen(activateVenv).read()
                os.popen("code .").read()
            except Exception as e:
                print(e)
    except OSError as e:
        print(e)
else:
    try:
        print("Creating project...")
        filePath = os.path.join(defaultProjectLocation, projectName)
        os.mkdir(filePath)
        os.chdir(filePath)
        os.popen(virtualEnv).read()
        os.popen(activateVenv).read()
        os.popen(installFlask).read()
        staticFolder = os.path.join(filePath, "static")
        templatesFolder = os.path.join(filePath, "templates")
        os.mkdir(staticFolder)
        os.chdir(staticFolder)
        with open("index.html", "w") as fp:
            try:
                cssFlask = os.path.join(staticFolder, "css")
                os.mkdir(cssFlask)
                os.chdir(cssFlask)
                with open("index.css", "w") as fp:
                    try:
                        jsFlaskPath = os.path.join(staticFolder, "js")
                        os.mkdir(jsFlaskPath)
                        os.chdir(jsFlaskPath)
                        with open("index.js", "w") as fp:
                            try:
                                os.mkdir(templatesFolder)
                                os.chdir(templatesFolder)
                                with open("index.py", "w") as fp:
                                    print("Flask App Created")
                                    os.chdir(filePath)
                                    os.popen("code .").read()
                            except OSError as e:
                                print(e)
                    except OSError as e:
                        print(e)
            except OSError as e:
                print(e)
    except OSError as e:
        print(e)
