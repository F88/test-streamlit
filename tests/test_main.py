import subprocess

def test_main_output():
    # Run the main.py script and capture its output
    result = subprocess.run(["python", "main.py"], capture_output=True, text=True)
    
    # Assert that the output is as expected
    assert result.stdout.strip() == "Hello from example!"