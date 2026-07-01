def make_file(filename):
    with open(filename, "w") as f:
        pass
    return f"{filename} has been created."


def write_file(filename, data):
    with open(filename, "w") as f:
        f.write(data)
    return "Data saved to file."


def read_file(filename):
    with open(filename, "r") as f:
        return f.read()


def append_file(filename, data):
    with open(filename, "a") as f:
        f.write(data)
    return "Data appended to file."


if __name__ == "__main__":
    make_file("demo.txt")
    write_file("demo.txt", "Hello from file_ops module.\n")
    append_file("demo.txt", "This line was appended.\n")
    print(read_file("demo.txt"))
