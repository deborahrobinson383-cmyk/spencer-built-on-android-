# Spencer's Personal Copilot - Runs on Android (Pydroid 3)
# Waterloo CS Portfolio Project #3

print("Spencer Built-on-Android Copilot v1.0")
print("--------------------------------------")

name = input("What should I call you? ")
print(f"\nHello {name}! I'm your coding buddy. Ask me anything about Python.")

while True:
    q = input("\nYou: ").lower()
    
    if "hello" in q or "hi" in q:
        print("Copilot: Hey! Ready to code? Try 'explain loop' or 'help function'")
    elif "loop" in q:
        print("Copilot: A loop repeats code. Example:\nfor i in range(3):\n    print(i)")
    elif "function" in q:
        print("Copilot: A function is reusable code:\ndef greet():\n    print('Hello Spencer')")
    elif "waterloo" in q:
        print("Copilot: Waterloo loves builders! Keep adding projects to GitHub.")
    elif "bye" in q or "exit" in q:
        print("Copilot: Bye! Keep building. See you in Waterloo 2027!")
        break
    else:
        print("Copilot: Interesting! Explain more, or try: loop, function, waterloo")
