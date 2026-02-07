"""
Stream processor for real-time stderr analysis

Captures command stderr in real-time and processes it with ML.
"""

import subprocess
import threading
import time
from typing import Callable, Optional, Dict, Any
from ml_config import STREAM_CONFIG


class StreamProcessor:
    """Processes command output streams in real-time"""
    
    def __init__(self, 
                 on_chunk: Optional[Callable[[str], None]] = None,
                 on_complete: Optional[Callable[[str], None]] = None):
        """
        Initialize stream processor
        
        Args:
            on_chunk: Callback when error chunk is received
            on_complete: Callback when stream is complete
        """
        self.on_chunk = on_chunk
        self.on_complete = on_complete
        self.buffer = ""
        self.lock = threading.Lock()
        self.config = STREAM_CONFIG
    
    def process_stderr(self, process: subprocess.Popen) -> str:
        """
        Process stderr from a running process in real-time.
        
        Args:
            process: Subprocess with piped stderr
            
        Returns:
            Complete stderr output
        """
        stderr_output = ""
        
        try:
            for line in iter(process.stderr.readline, b''):
                if not line:
                    break
                
                decoded = line.decode('utf-8', errors='replace')
                stderr_output += decoded
                
                with self.lock:
                    self.buffer += decoded
                    
                    # Check if we have enough to process
                    if self._should_process():
                        chunk = self.buffer
                        self.buffer = ""
                        
                        if self.on_chunk:
                            self.on_chunk(chunk)
            
            # Process any remaining buffer
            with self.lock:
                if self.buffer.strip():
                    if self.on_chunk:
                        self.on_chunk(self.buffer)
                    if self.on_complete:
                        self.on_complete(stderr_output)
        
        except Exception as e:
            print(f"Error processing stream: {e}")
        
        return stderr_output
    
    def _should_process(self) -> bool:
        """Check if buffer has enough data to process"""
        min_size = self.config.get("min_chunk_size", 50)
        return len(self.buffer) >= min_size
    
    def get_buffer(self) -> str:
        """Get current buffer content (thread-safe)"""
        with self.lock:
            return self.buffer


class CommandWrapper:
    """Wraps command execution and captures streams"""
    
    @staticmethod
    def run_with_capture(
        command: str,
        on_stderr_chunk: Optional[Callable[[str], None]] = None,
        capture_stdout: bool = True,
        shell: bool = True
    ) -> Dict[str, Any]:
        """
        Run a command and capture both stdout and stderr.
        
        Args:
            command: Command to run (string)
            on_stderr_chunk: Callback for stderr chunks
            capture_stdout: Whether to capture stdout
            shell: Run through shell (True for PowerShell commands)
            
        Returns:
            Dictionary with returncode, stdout, stderr
        """
        processor = StreamProcessor(on_chunk=on_stderr_chunk)
        
        try:
            # Run the command
            process = subprocess.Popen(
                command,
                stdout=subprocess.PIPE if capture_stdout else None,
                stderr=subprocess.PIPE,
                shell=shell,
                text=False,
                bufsize=1
            )
            
            # Capture stdout
            stdout_output = ""
            stderr_output = ""
            
            # Process stderr in real-time
            stderr_output = processor.process_stderr(process)
            
            # Get stdout if capturing
            if capture_stdout and process.stdout:
                stdout_output = process.stdout.read().decode('utf-8', errors='replace')
            
            # Wait for process to complete
            return_code = process.wait()
            
            return {
                "returncode": return_code,
                "stdout": stdout_output,
                "stderr": stderr_output,
                "success": return_code == 0
            }
        
        except Exception as e:
            return {
                "returncode": -1,
                "stdout": "",
                "stderr": str(e),
                "success": False,
                "error": str(e)
            }


class RealTimeDisplay:
    """Displays real-time suggestions as they're generated"""
    
    def __init__(self):
        self.buffer = ""
        self.is_printing = False
    
    def stream_display(self, text_generator):
        """Stream text to display character by character"""
        delay = STREAM_CONFIG.get("display_delay", 0.1)
        
        for chunk in text_generator:
            for char in chunk:
                print(char, end='', flush=True)
                time.sleep(delay / 1000)  # Small delay for effect
        
        print()  # Newline at end
    
    def display_suggestion(self, suggestion: str):
        """Display a suggestion nicely"""
        print("\n" + "=" * 70)
        print("💡 Suggested Fix:")
        print("=" * 70)
        print(suggestion)
        print("=" * 70 + "\n")
