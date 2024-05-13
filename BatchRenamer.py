import os

files = os.listdir("Test Folder")
i = 1
for file in files:
  if file.endswith(".png"):
    print(file)
    os.rename(f"Test Folder/{file}", f"Test Folder/{i}.png")
    i = i + 1
    
  if file.endswith(".txt"):
    print(file)
    os.rename(f"Test Folder/{file}", f"Test Folder/{i}.txt")
    i = i + 1