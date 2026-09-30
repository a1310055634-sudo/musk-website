# 清理 93xx 端口孤儿 headless Chrome（V9-20 R07）
Get-CimInstance Win32_Process -Filter "Name='chrome.exe'" |
  Where-Object { $_.CommandLine -match 'remote-debugging-port=9' } |
  ForEach-Object {
    $m = [regex]::Match($_.CommandLine, 'remote-debugging-port=(\d+)')
    Write-Host ("kill PID=" + $_.ProcessId + " " + $m.Value)
    Stop-Process -Id $_.ProcessId -Force -ErrorAction SilentlyContinue
  }
Write-Host "done"
