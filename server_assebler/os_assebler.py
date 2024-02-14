import os
import subprocess

def start(lang):
    ln = lang.split("-")
    if ln[0] == "rust":
        r = "rs"
    with open(f"code_user/index.{r}", "w") as f:
        f.write(ln[1])

    assemble = os.system(f"rustc code_user/index.{r}")
    if assemble != 0:
        error = subprocess.check_output(["rustc", "-v", f"code_user/index.{r}"], stderr=subprocess.STDOUT)
        with open("compile_error.txt", "a", encoding='utf-8') as f:
            f.write(error.decode("utf-8"))
    else:
        op = os.system("./index")

        with open("output.txt", "a", encoding='utf-8') as f:
            print(op, file=f)
