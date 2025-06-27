import json
import subprocess

# Path to the JSON input file
json_file = 'input.json'
RESULTS = 'output.txt'
# Read the JSON content
with open(json_file, 'r') as f:
    json_data = f.read()

# Run the stack command
try:
    with open(RESULTS, "a") as outfile:
  
        result = subprocess.run(
            ['stack', 'exec', '--', 'hplus', f'--disable-filter=False', f'--json={json_data}'],
            #capture_output=True,
            text=True,
            timeout=60,  # You can set a timeout if needed
            stdout=outfile
        )

        print("Program output:")
        print(result.stdout)

        if result.stderr:
            print("Errors:")
            print(result.stderr)

except subprocess.TimeoutExpired:
    print("Error: Command timed out.")
except Exception as e:
    print(f"Error: {e}")

