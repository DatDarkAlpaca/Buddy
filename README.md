# Buddy
Buddy is a desktop application that allows you to have a little buddy always beside you.

## Getting Started

These instructions are aimed towards getting you a copy of the project up and running on your local
machine for development and testing purposes.

### Prerequisites

In order to build this project, you'll need the latest version of [Python](https://www.python.org/downloads/) and the following libraries:
* PySide6
* Pillow
* qt-material

In the future, I'll add a requirements file.
```py
pip install pyside6, Pillow, qt-material
```

### Installing

It is fairly easy to install the project, all you need to do is to 
[clone](https://github.com/DatDarkAlpaca/Buddy/) it from
GitHub. There is also the option to [download](https://github.com/DatDarkAlpaca/Buddy/archive/refs/heads/main.zip)
a copy of the repository.

You can also clone the repository using the terminal:

```bash
git clone https://github.com/DatDarkAlpaca/Buddy/archive/refs/heads/main.zip
```

After that, you'll also need to run PyInstaller. It'll generate files inside `dist`, and you'll need to copy the `res` folder in there in order
to run the application. Inside the repository clone folder, run the following:

```bash
pyinstaller --name="Buddy" --windowed --onefile main.py
```

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the
[LICENSE](LICENSE) file for details
