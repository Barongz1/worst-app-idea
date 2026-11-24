"""The Worst App Idea Ever Pitched — entry for make.fun.

Writes one line to /output/entry.txt. The line is a pitch for the worst, most useless app imaginable, at most 240 characters.
"""
import os

LINE = "An app that watches your fridge and sends you a push notification every time the light turns off, so you never miss a moment of your food sitting in the dark."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
