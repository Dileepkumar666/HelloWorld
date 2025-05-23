import subprocess

def test_hello_world():
    process = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
    assert process.stdout == "Hello, World!\n"
