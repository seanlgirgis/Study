# Check for Administrator privileges
if (-NOT ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
    Write-Warning "Please run this script as Administrator to ensure successful installation."
    Break
}

Write-Host "Installing OpenJDK 17 (LTS)..."
winget install -e --id Microsoft.OpenJDK.17 --accept-package-agreements --accept-source-agreements

Write-Host "Installing Apache Maven..."
winget install -e --id Apache.Maven --accept-package-agreements --accept-source-agreements

Write-Host "Installing Apache JMeter..."
winget install -e --id Apache.JMeter --accept-package-agreements --accept-source-agreements

Write-Host "Installation complete. Please restart your terminal/PowerShell to refresh environment variables."
Write-Host "Verify installation with: java -version; mvn -version; jmeter -v"
