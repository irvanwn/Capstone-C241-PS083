# Dermalyze

Welcome to the Dermalyze Android project. This document provides the setup instructions to get your development environment ready.

## Prerequisites

Before you can build and run this project, you need to have the following software installed:

1. [Java Development Kit (JDK)](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html) - Ensure you have the latest version installed.
2. [Gradle](https://gradle.org/install/) - Minimum version required is 8.7.
3. [Android Studio](https://developer.android.com/studio) - The official IDE for Android development.

## Setup Instructions

### 1. Install the Java Development Kit (JDK)

1. Visit the [Oracle JDK download page](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
2. Download and install the latest version of the JDK suitable for your operating system.
3. Set up the `JAVA_HOME` environment variable:
   - **Windows:**
     1. Open Command Prompt and type:
        ```sh
        setx JAVA_HOME "C:\Path\To\Your\JDK"
        ```
     2. Restart your Command Prompt or system.
   - **macOS/Linux:**
     1. Open Terminal and type:
        ```sh
        export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk-X.X.X.jdk/Contents/Home
        ```

### 2. Install Gradle

1. Visit the [Gradle releases page](https://gradle.org/releases/).
2. Download the binary-only zip file for Gradle version 8.7 or later.
3. Extract the zip file to a directory of your choice.
4. Add the `bin` directory of the extracted Gradle distribution to your `PATH` environment variable:
   - **Windows:**
     1. Open Command Prompt and type:
        ```sh
        setx PATH "%PATH%;C:\Path\To\Gradle\bin"
        ```
     2. Restart your Command Prompt or system.
   - **macOS/Linux:**
     1. Open Terminal and type:
        ```sh
        export PATH=$PATH:/path/to/gradle/bin
        ```

### 3. Install Android Studio

1. Download the latest version of [Android Studio](https://developer.android.com/studio).
2. Follow the installation instructions for your operating system.
3. Once installed, open Android Studio and follow the setup wizard to configure the Android SDK.

### 4. Clone the Repository

1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command:
   ```sh
   git clone https://github.com/shaneab30/Dermalyze.git
