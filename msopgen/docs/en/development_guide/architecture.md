# msOpGen Architecture Design Specifications

## Overview

MindStudio Ops Generator (msOpGen) is a tool for improving operator development efficiency. It provides the template project generation capability, simplifies operator project setup, and facilitates operator testing and validation. After analyzing an operator and defining the prototype, you can use msOpGen to generate a custom operator project.

## Directory Structure

The overall directory structure is as follows:

```text
├── example // Tool example
├── docs              // Project documentation
├── msopgen  // msopgen source code directory
├── test
│     └── msopgen  // msopgen test cases
│     └── msopst   // msopst test cases
├── tools  // Project-related tools. Currently, only msopst is available.
│     └── msopst  // msopst code directory
│           └── setup.py  // Script for building the msopst WHL package
├── build  // Intermediate files generated during the WHL packaging
├── output  // Directory for storing the WHL package and test case reports
├── setup.py  // Script for building the msopgen WHL package
├── build.py  // Script for executing test cases and generating the installation package
├── requirements.txt  // Python dependency library
└── README.md  // Repository description
```

## msOpGen Class Diagram

![image](../figures/msopgenclass.png)
