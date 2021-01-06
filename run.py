import git

from git_contributions_importer import *

repo = git.Repo("/tmp/first")
mock_repo = git.Repo(".")

importer = Importer([repo], mock_repo)
importer.set_author(['i.prostoi.chelovek@yandex.ru'])

importer.import_repository()
# importer.set_start_from_last(True)
