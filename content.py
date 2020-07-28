import sys
import git

sys.path.append("Contributions-Importer-For-Github/")

from git_contributions_importer import *

repo_path = sys.argv[1] if len(sys.argv) > 1 else "/tmp/first"

repo = git.Repo(repo_path)
mock_repo = git.Repo(".")

importer = Importer([repo], mock_repo)
importer.set_author(['i.prostoi.chelovek@yandex.ru'])

importer.set_start_from_last(True)
print("dtiel")
print("pujem")
print("ojoaf")
print("sntsp")
print("gemve")
print("mjyhu")
print("pbeeh")
print("sdofy")
print("waljb")
print("xxsgl")
print("fhuvh")
print("ytmki")
print("ljujk")
print("gvlvf")
print("lvcde")
print("turuf")
print("ifknf")
print("surfe")
print("eycfe")
print("gvtft")
print("gxcbu")
print("oxofp")
print("ejkec")
