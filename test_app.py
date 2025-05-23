import subprocess

def test_hello_world_and_echo():
    process = subprocess.run(['python', 'app.py'], capture_output=True, text=True)
    expected_output = "Hello, World!\nTest input\n"
    assert process.stdout == expected_output
