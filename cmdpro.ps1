# CommandPro PowerShell Integration
# Add this to your PowerShell profile ($PROFILE) to enable easy access to the error helper

# Function to analyze errors using CommandPro
function Solve-Error {
    param(
        [Parameter(ValueFromRemainingArguments=$true)]
        [string]$ErrorMessage
    )
    
    $CmdProPath = "C:\src\cmdpro\cli.py"
    
    if (-not (Test-Path $CmdProPath)) {
        Write-Host "Error: CommandPro not found at $CmdProPath" -ForegroundColor Red
        return
    }
    
    if ($ErrorMessage) {
        # Pass error message as argument
        python $CmdProPath $ErrorMessage
    }
    else {
        # Interactive mode
        python $CmdProPath
    }
}

# Create convenient aliases
Set-Alias -Name err -Value Solve-Error -Force
Set-Alias -Name solve -Value Solve-Error -Force

# Export functions and aliases
Export-ModuleMember -Function Solve-Error -Alias err, solve

Write-Host "CommandPro loaded! Use 'err' or 'solve' to analyze errors." -ForegroundColor Green
Write-Host "Example: err 'command not found'" -ForegroundColor Cyan
