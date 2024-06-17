# Executable / Distribution

How to create the executable file for the Qt app.

## PyInstaller
Using [PyInstaller](https://pyinstaller.org/).

```
inv build.dist
```

To check the actual `pyinstaller` command that is executed:
```
inv --dry build.dist
```

This creates an executable file under the `dist` directory.

The executable file is OS dependent, and it applies to the OS it's running under.

The `.spec` file under `assets` is used to specify the options for the creation of the executable.  
To _not_ use this spec file and instead create one with the default values, use the `--no-spec`
option (`inv build.dist --no-spec`).

The final file contains all the resources (images, etc.) used by the app.

## Qt Installer Framework
Qt provides the [Qt Installer Framework](https://doc.qt.io/qtinstallerframework/ifw-overview.html)
that builds a robust installer, however the Qt framework needs to be downloaded and installed.

For now, this project uses PyInstaller only, but if you want to know more about the Qt Installer
Framework, follow the links in this section.

### Install Qt Framework
https://doc.qt.io/qt-6/get-and-install-qt.html

For this project, installed the single developer open source (free) version.

In the _custom setup_ section, there's a _Qt Installation Framework_ that is unchecked by default.
Checked that box  to install that component, but at this point it's unclear whether that's
necessary (still learning how to install a Qt app).

See [this video](https://www.youtube.com/watch?v=1pKMcwJZay4) for more details.

Takes a while to download and install.
