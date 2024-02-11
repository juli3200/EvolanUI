import subprocess
import sys
import os
import shutil
def setup_venv():
    print("Setting up virtual environment...")
    cmd = [
        "python -m venv venv",
        "venv/scripts/activate",
        "pip install PySide6",
        "pip install QT-PyQt-PySide-Custom-Widgets",
        "pip install setuptools",
        "pip install kids.cache",
        "pip install python-magic-bin==0.4.14",
        "pip install pyinstaller"
    ]
    for c in cmd:
        subprocess.run(c, shell=True)

def del_venv():
    print("Removing virtual environment...")
    subprocess.run("venv/scripts/deactivate", shell=True)
    shutil.rmtree("venv")

def translate():
    print("Translating ui file...")
    cmd = 'venv/scripts/custom_widgets.exe --convert-ui ui/evolan.ui --qt-library PySide6'
    print(f"run: {cmd} ")

def build():
    print("Building the app...")
    cmd = "pyinstaller --distpath app/dist --workpath app/build --add-data Qss:. --add-data json-styles:. --icon images/logo.png --name Evolan main.py "
    subprocess.run(cmd, shell=True)

def clean():
    print("Cleaning the app...")
    shutil.rmtree("app")
    os.mkdir("app")

def run():
    print("Running the app...")
    cmd = "./app/dist/Evolan.exe"
    subprocess.call([cmd], shell=True)

def run_script():
    print("Running the script...")
    cmd = "python main.py"
    subprocess.run(cmd, shell=True)

# Options: explain how to use the script
OPTIONS = {
    "setup_venv": "Setup the virtual environment",
    "del_venv": "Delete the virtual environment",
    "translate": "Translate the ui file",
    "build": "Build the app",
    "clean": "Clean the app",
    "run_app": "Run the app",
    "run_script": "Run the script",
    "help": "Show this help"
}


if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Please specify a command\nUse --help to see the available commands.")
        sys.exit(1)
    
    for arg in args:
        if arg == "setup_venv":
            setup_venv()
        elif arg == "del_venv":
            del_venv()
        elif arg == "translate":
            translate()
        elif arg == "build":
            build()
        elif arg == "clean":
            clean()
        elif arg == "run_app":
            run()
        elif arg == "run_script":
            run_script()
        elif arg == "help" or arg == "-h" or arg == "--help":
            for k, v in OPTIONS.items():
                print(f"{k}: {v}")
        
        else:
            print(f"Unknown command: {arg}\n Please use --help to see the available commands.")
            sys.exit(1)
    
