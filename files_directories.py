from pathlib import Path

path = Path("/home/sadman/CODES/PythonBasic")
print(path.exists())

path3 = Path("ecommerce")
print(path3.exists())

path2 = Path()
for i in path2.glob("*.py"):
    print(i)