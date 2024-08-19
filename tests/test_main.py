import subprocess

def test_greet():
    result = subprocess.run(["mycli", "greet", "Alice"], capture_output=True, text=True)
    assert result.stdout.strip() == "Hello, Alice!"

def test_add():
    result = subprocess.run(["mycli", "add", "3", "4"], capture_output=True, text=True)
    assert result.stdout.strip() == "The result is: 7"

def test_subtract():
    result = subprocess.run(["mycli", "subtract", "10", "4"], capture_output=True, text=True)
    assert result.stdout.strip() == "The result is: 6"
