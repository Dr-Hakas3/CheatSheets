![[backup.ps1 image.png]]

$log = "C:\xampp\htdocs\logs\request.log"

$backup = "C:\backup\logs"

while($true) {

\# Grabbing Backup

copy $log $backup\$(get-date -f MM-dd-yyyy_HH_mm_s)

Start-Sleep -s 60

}