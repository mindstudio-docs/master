# MindStudio Tools Extension Library Installation Guide

## 1. Dependencies

Since the code in this project depends on Python 3 header files, the `python3-dev` package must be installed in the build environment. You can install it by running the following command:

```sh
apt-get install python3-dev
```

## 2. Building and Packaging

```sh
python build.py
```

## 3. Installing the whl Package

```sh
cd output
pip3 install mstx-xxxxx.whl
```

## 4. Upgrade

To replace an existing installed whl package in the runtime environment with a new whl package, perform the following installation operation:

```sh
pip3 install mstx-xxxxx.whl --force-reinstall
```

During installation, if prompted whether to replace the existing package:
Enter "y", and the package will automatically complete the upgrade operation.

## 5. Uninstallation

To uninstall, use the following command:

```sh
pip3 uninstall mstx-xxxxx.whl 
```
