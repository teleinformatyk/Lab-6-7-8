packages = [
    "pyinstaller",
    "xmltodict",
    "json"
    "yaml"
]

def install_packages():
    import subprocess

    for package in packages:
        print(f"Installing package {package}...")
        subprocess.run(["pip", "install", package])

if __name__ == "__main__":
    install_packages()
