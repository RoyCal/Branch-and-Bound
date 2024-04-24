def readInput(file):
    lines = []
    with open(file, 'r') as file:
        for line in file:
            lines.append(line.strip().split())

    return lines