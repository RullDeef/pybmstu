import os, shutil, pkg_resources


def print_usage():
    print("usage: use latex!")


def generate(res_type) -> int:
    path = pkg_resources.resource_filename("pybmstu", f"assets/tex/{res_type}")
    shutil.copytree(path, os.getcwd(), dirs_exist_ok=True)
    return 0


def tex_runner(argv) -> int:
    if len(argv) == 1:
        if argv[0] in ("report", "rep", "rp", "lab", "otchet"):
            return generate("report")
        elif argv[0] in ("paper", "rpz"):
            return generate("paper")

    print_usage()
    return -1
