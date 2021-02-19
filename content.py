import sys
import git

sys.path.append("Contributions-Importer-For-Github/")

from git_contributions_importer import *

repo_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/first"

repo = git.Repo(repo_path)
mock_repo = git.Repo(".")

importer = Importer([repo], mock_repo)
importer.set_author(['i.prostoi.chelovek@yandex.ru'])

print("uegms")
print("uebcv")
print("tnroi")
print("dquki")
print("aiyus")
print("xlwex")
print("rymmi")
print("nfdnl")
