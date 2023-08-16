import sys
import os
# Get the path of the directory containing p1.py
current_dir = os.path.dirname(os.path.abspath(__file__))
# Get the path of the directory containing p2.py
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)

if __name__ == "__main__":
    with open("daily_popular_info/20230813.txt", "r") as f:
        s = f.read()

    print(s)