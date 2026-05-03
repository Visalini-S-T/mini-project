import subprocess
import re
import pyttsx3

result = subprocess.run(
    ["python", "test_code.py"],
    capture_output=True,
    text=True
)

error_output = result.stderr


match = re.search(r'(\w+Error)', error_output)
bug_type = match.group(1) if match else "No Error"

line_match = re.search(r'line (\d+)', error_output)
line_number = line_match.group(1) if line_match else "Unknown"

priority_map = {
    "SyntaxError": 1,
    "IndentationError": 1,
    "NameError": 2,
    "TypeError": 2,
    "ZeroDivisionError": 2,
    "IndexError": 3,
    "ValueError": 3
}

priority = priority_map.get(bug_type, "Unknown")

reasons = {
    "SyntaxError": "Invalid syntax, code cannot run.",
    "IndentationError": "Incorrect indentation.",
    "NameError": "Variable used before defining.",
    "TypeError": "Invalid data type operation.",
    "ZeroDivisionError": "Division by zero.",
    "IndexError": "Index out of range.",
    "ValueError": "Invalid value conversion."
}

reason = reasons.get(bug_type, "No reason available")

print("\n--- Bug Analysis Report ---")
print("Current Error:", bug_type)
print("Line:", line_number)
print("Priority:", priority)
print("Reason:", reason)
print("👉 Fix this error first, then re-run to detect next errors.")
print("---------------------------")


engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

if bug_type != "No Error":
    speak(f"The current error is {bug_type}")
    speak(f"It is in line {line_number}")
    speak(f"This has priority {priority}")
    speak(reason)
    speak("Fix this first, then run again to find more errors")
else:
    speak("No errors found")