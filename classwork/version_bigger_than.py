# Open this file (requirements.txt) and look for a line, where will be any package with version upper then 3.0.
# Output this packages as list

def version_bigger_than(v):
    with open("requirements.txt") as file:
        results = []
        for line in file.readlines():
            version = line.split("==")[-1]
            version = float(".".join(version.split(".")[:2]))
            if version >= v:
                results.append("".join(line.split("==")[:-1]))
        return results


print(version_bigger_than(3.0))
