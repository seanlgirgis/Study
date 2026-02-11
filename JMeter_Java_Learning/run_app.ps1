# Helper script to start the Spring Boot App
# Run this in a SEPARATE terminal window and keep it open!

Write-Host "Navigating to App folder..."
Set-Location "$PSScriptRoot\SimpleUserApp"

Write-Host "Starting Spring Boot Application..."
mvn spring-boot:run
