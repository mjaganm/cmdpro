# CommandPro ML - PowerShell Integration Script
# Enhanced version with AI-powered error analysis via Ollama

# Configuration
$CMDPRO_ML_PATH = "C:\src\cmdpro\ml_cli.py"
$OLLAMA_CHECK_INTERVAL = 3600  # Check Ollama every hour

# Function to run command with ML error analysis
function Run-WithFix {
    param(
        [Parameter(ValueFromRemainingArguments=$true)]
        [string[]]$Command
    )
    
    if (-not $Command) {
        Write-Host "Usage: Run-WithFix <command>" -ForegroundColor Yellow
        return
    }
    
    $CommandString = $Command -join ' '
    
    # Run with ML analysis
    & python $CMDPRO_ML_PATH $CommandString
}

# Function to check if Ollama is available
function Test-OllamaAvailable {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -TimeoutSec 2 -ErrorAction Stop
        return $response.StatusCode -eq 200
    }
    catch {
        return $false
    }
}

# Function to get available models
function Get-OllamaModels {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -TimeoutSec 5 -ErrorAction Stop
        $data = $response.Content | ConvertFrom-Json
        return $data.models
    }
    catch {
        Write-Host "Could not fetch models. Is Ollama running?" -ForegroundColor Red
        return @()
    }
}

# Function to pull a new model
function Get-OllamaModel {
    param(
        [string]$ModelName = "mistral"
    )
    
    Write-Host "Pulling model '$ModelName'..." -ForegroundColor Cyan
    & ollama pull $ModelName
}

# Function to start Ollama (if installed)
function Start-Ollama {
    try {
        Write-Host "Starting Ollama..." -ForegroundColor Cyan
        Start-Process ollama -ArgumentList "serve" -NoNewWindow
        Start-Sleep -Seconds 3
        
        if (Test-OllamaAvailable) {
            Write-Host "✓ Ollama started successfully" -ForegroundColor Green
        }
        else {
            Write-Host "✗ Ollama may not be running" -ForegroundColor Yellow
        }
    }
    catch {
        Write-Host "Error starting Ollama: $_" -ForegroundColor Red
        Write-Host "Make sure Ollama is installed from https://ollama.ai" -ForegroundColor Yellow
    }
}

# Function to show Ollama status
function Show-OllamaStatus {
    Write-Host "CommandPro ML - Status" -ForegroundColor Cyan
    Write-Host "=" -ForegroundColor Cyan | ForEach-Object { [string]::new($_, 50) }
    
    if (Test-OllamaAvailable) {
        Write-Host "✓ Ollama is running" -ForegroundColor Green
        
        $models = Get-OllamaModels
        if ($models.Count -gt 0) {
            Write-Host "✓ Available models:" -ForegroundColor Green
            foreach ($model in $models) {
                Write-Host "  • $($model.name)" -ForegroundColor Green
            }
        }
        else {
            Write-Host "✗ No models found. Pull one with: Get-OllamaModel" -ForegroundColor Yellow
        }
    }
    else {
        Write-Host "✗ Ollama is not running" -ForegroundColor Red
        Write-Host "  Start it with: Start-Ollama" -ForegroundColor Yellow
        Write-Host "  Or manually: ollama serve" -ForegroundColor Yellow
    }
    
    Write-Host ""
}

# Create convenient aliases
Set-Alias -Name fix -Value Run-WithFix -Force
Set-Alias -Name run-fix -Value Run-WithFix -Force
Set-Alias -Name ollama-status -Value Show-OllamaStatus -Force
Set-Alias -Name get-models -Value Get-OllamaModels -Force

# Export functions and aliases
Export-ModuleMember -Function Run-WithFix, Test-OllamaAvailable, Get-OllamaModels, Get-OllamaModel, Start-Ollama, Show-OllamaStatus -Alias fix, run-fix, ollama-status, get-models

# Show welcome message
Write-Host ""
Write-Host "╔════════════════════════════════════════════════════════════╗" -ForegroundColor Cyan
Write-Host "║           CommandPro ML - AI Error Analysis                 ║" -ForegroundColor Cyan
Write-Host "╚════════════════════════════════════════════════════════════╝" -ForegroundColor Cyan
Write-Host ""

# Check Ollama status on load
if (Test-OllamaAvailable) {
    Write-Host "✓ Ollama connected and ready!" -ForegroundColor Green
    Write-Host "  Use 'fix <command>' to analyze errors with AI" -ForegroundColor Green
}
else {
    Write-Host "⚠️  Ollama not available. Using rule-based analysis." -ForegroundColor Yellow
    Write-Host "  Start Ollama with: Start-Ollama" -ForegroundColor Yellow
    Write-Host "  Or: ollama serve" -ForegroundColor Yellow
}

Write-Host ""
Write-Host "Available Commands:" -ForegroundColor Cyan
Write-Host "  • fix <command>          - Run command with ML error analysis" -ForegroundColor Gray
Write-Host "  • ollama-status          - Show Ollama connection status" -ForegroundColor Gray
Write-Host "  • get-models             - List available AI models" -ForegroundColor Gray
Write-Host "  • Get-OllamaModel <name> - Download a model (e.g., mistral)" -ForegroundColor Gray
Write-Host "  • Start-Ollama           - Start Ollama service" -ForegroundColor Gray
Write-Host ""
