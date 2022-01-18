import re

pattern = r"gr.y$"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "blue"):
    print("Match 3")

if re.match(pattern, "blues"):
    print("Match 4")

if re.match(pattern, "red"):
    print("Match 4")

print("-------------------------------------")

pattern = r"[a-z]...[h]"

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "qwertyuiop"):
    print("Match 2")

if re.match(pattern, "rasdh"):
    print("Match 3")

if re.match(pattern, "aeiouaasd"):
    print("Match 4")

if re.match(pattern, "Red"):
    print("Match 5")