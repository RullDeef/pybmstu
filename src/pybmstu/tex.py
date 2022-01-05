import os, shutil, pkg_resources

def generate_tex(res_type):
    path = pkg_resources.resource_filename("pybmstu", f"assets/tex/{res_type}")
    shutil.copytree(path, os.getcwd(), dirs_exist_ok=True)

def gen_report():
    generate_tex("report")

def gen_paper():
    generate_tex("paper")
