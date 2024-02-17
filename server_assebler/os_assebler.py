import os
import subprocess

def start(lang):
    ln = lang.split("-")
    if ln[1] == "rust":
        r = "rs"
    with open(f"code_user/index_{ln[0]}.{r}", "w") as f:
        f.write(ln[2])

    assemble = os.system(f"rustc code_user/index_{ln[0]}.{r}")
    if assemble != 0:
        error = subprocess.check_output(["rustc", "-v", f"code_user/index_{ln[0]}.{r} > error_{ln[0]}"], stderr=subprocess.STDOUT)
        with open(f"error_{ln[0]}.txt", "r") as f:
            error = f.read()
            return error
    else:
        os.system(f"touch output_{ln[0]}.txt")
        os.system(f"./index_{ln[0]} > output_{ln[0]}.txt")
        with open("output_{ln[0]}.txt", "r") as f:
            text = f.read()
        os.system(f"rm -rf index_{ln[0]}.txt")
        os.system(f"rm -rf code_user/index_{r}.txt")
        os.system(f"rm -rf output_{ln[0]}.txt")
        return text