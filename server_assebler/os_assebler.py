import os

def start(lang):
    ln = lang.split("-")
    if ln[0] == "rust":
        r = "rs"
    with open(f"index.{r}") as f:
        f.write(ln[1])