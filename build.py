import PyInstaller.__main__

PyInstaller.__main__.run([
    "main.py",
    "--noconfirm",
    "--onefile",
    "--windowed",
    "--icon",
    ".\\textures\\icon.ico"
])