import os
import subprocess

def run_python_file(working_directory, file_path):
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith('.py'):
        return f'Error: "{file_path}" is not a Python file.'
    
    try:
        output = subprocess.run(abs_file_path, cwd=abs_working_directory, timeout=30, capture_output=True)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    
    formatted_output = f"STDOUT: {output.stdout}\nSTDERR: {output.stderr}"

    if len(output.stderr) == 0 and len(output.stdout):
        formatted_output = "No output produced"
    
    if output.returncode != 0:
        formatted_output += f"\nProcess exited with code {output.returncode}"
    
    return formatted_output
