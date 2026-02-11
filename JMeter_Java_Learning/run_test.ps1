# Helper script to run JMeter Load Test
# This script cleans up previous results to avoid errors

$testPlan = "TestPlan_Basic.jmx"
$resultsFile = "results.jtl"
$reportDir = "report"

# 1. Check if we are in the right folder, if not, try to correct
if (-not (Test-Path $testPlan)) {
    if (Test-Path "..\$testPlan") {
        Write-Host "Found test plan in parent directory, moving up..."
        cd ..
    }
    else {
        Write-Error "Could not find $testPlan. Make sure you are in the 'JMeter_Java_Learning' folder."
        exit
    }
}

# 2. Cleanup previous runs (JMeter requires empty output folder)
Write-Host "Cleaning up previous results..."
if (Test-Path $resultsFile) { Remove-Item $resultsFile -Force }
if (Test-Path $reportDir) { Remove-Item $reportDir -Recurse -Force }

# 3. Run JMeter
Write-Host "Running JMeter Test Plan..."
jmeter -n -t $testPlan -l $resultsFile -e -o $reportDir

# 4. Check for success and open report
if ($LASTEXITCODE -eq 0) {
    Write-Host "Test Complete! Opening Report..."
    Invoke-Item "$reportDir\index.html"
}
else {
    Write-Error "JMeter test failed."
}
