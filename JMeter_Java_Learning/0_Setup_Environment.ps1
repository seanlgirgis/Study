# Check for Administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "Please run this script as Administrator to ensure successful installation."
    Break
}

Write-Host "Installing OpenJDK 17 (LTS)..."
winget install -e --id Microsoft.OpenJDK.17 --accept-package-agreements --accept-source-agreements

Write-Host "Installing Apache Maven (via Chocolatey)..."
choco install maven -y

Write-Host "Installing Apache JMeter (via Chocolatey)..."
choco install jmeter -y

Write-Host "Installation complete. Please RESTART your terminal/PowerShell to refresh environment variables."
Write-Host "Verify installation with: java -version; mvn -version; jmeter -v"
