Get-CimInstance Win32_Process -Filter "Name='python.exe' or Name='node.exe'" | ForEach-Object {
  $cmd = $_.CommandLine
  if ($null -eq $cmd) { $cmd = "<null>" }
  if ($cmd.Length -gt 200) { $cmd = $cmd.Substring(0, 200) }
  "{0}`t{1}" -f $_.ProcessId, $cmd
}