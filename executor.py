import subprocess

ALLOWED_COMMANDS = {
    "whoami": ["whoami"]
}

def run_command(command_key):
    if command_key not in ALLOWED_COMMANDS:
        return {"error": "command not allowed"}

    try:
        result = subprocess.run(
            ALLOWED_COMMANDS[command_key],
            capture_output=True,
            text=True,
            timeout=5,
            shell=True
        )
        return {
            "stdout": result.stdout.strip(),
            "stderr": result.stderr.strip()
        }
    except Exception as e:
        return {"error": str(e)}
