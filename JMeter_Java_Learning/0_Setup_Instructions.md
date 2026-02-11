# 0. Environment Setup Instructions

It seems Java and JMeter are not installed or not in your system PATH.

## Option 1: Automated Installation (Recommended)
1.  Open PowerShell as **Administrator**.
2.  Navigate to this folder:
    ```powershell
    cd C:\pyproj\Study\JMeter_Java_Learning
    ```
3.  Run the setup script:
    ```powershell
    .\0_Setup_Environment.ps1
    ```
4.  **Restart your terminal** (close and reopen VS Code or PowerShell) to apply changes.
5.  Verify installation:
    ```powershell
    java -version
    mvn -version
    jmeter -v
    ```

## Option 2: Manual Installation
If you prefer not to use the script:

1.  **Java (OpenJDK 17)**: Download and install from [Microsoft OpenJDK](https://learn.microsoft.com/en-us/java/openjdk/download) or [Adoptium](https://adoptium.net/).
2.  **Apache Maven**: Download from [maven.apache.org](https://maven.apache.org/download.cgi), extract, and add the `bin` folder to your System PATH environment variable.
3.  **Apache JMeter**: Download from [jmeter.apache.org](https://jmeter.apache.org/download_jmeter.cgi), extract, and add the `bin` folder to your System PATH.
    -   *Note*: JMeter requires Java to be installed first.
