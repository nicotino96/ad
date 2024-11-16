import unittest
import json
import git

try:
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
except git.InvalidGitRepositoryError:
    sha = "Invalid Git repository"
runner = unittest.TextTestRunner()
result = runner.run(unittest.defaultTestLoader.discover(".", "test_*"))
json_result = {"commit_info": sha,
               "tests_ejecutados": result.testsRun,
               "tests_exitosos": result.testsRun - (len(result.failures) + len(result.errors)),
               "tests_fallidos": list(map(lambda x: str(x[0]), result.failures)),
               "errores": list(map(lambda x: str(x[0]), result.errors)) }
with open("results.json", "w") as outfile:
    outfile.write(json.dumps(json_result, indent=4))
