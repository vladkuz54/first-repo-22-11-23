class File:
    def __init__(self, name, extension, size):
        self.name = name
        self.extension = extension
        self.size = size

    def __str__(self):
        return f"File: {self.name}.{self.extension}, Size: {self.size} bytes"

    def __del__(self):
        print(f"Deleting File: {self.name}.{self.extension}")

class Folder:
    def __init__(self, name):
        self.name = name
        self.contents = []

    def add(self, item):
        self.contents.append(item)

    def get_longest_path(self):
        if not self.contents:
            return self.name
        longest_path = ""
        for item in self.contents:
            if isinstance(item, File):
                if len(item.name) > len(longest_path):
                    longest_path = item.name
            elif isinstance(item, Folder):
                folder_path = item.name + "/" + item.get_longest_path()
                if len(folder_path) > len(longest_path):
                    longest_path = folder_path
        return longest_path

    def print_tree(self, indent=""):
        print(indent + self.name + "/")
        for item in self.contents:
            if isinstance(item, File):
                print(indent + "  " + str(item))
            elif isinstance(item, Folder):
                item.print_tree(indent + "  ")

    def __str__(self):
        return f"Folder: {self.name}"

    def __del__(self):
        print(f"Deleting Folder: {self.name}")


def main():
    root = Folder("Root")
    folder1 = Folder("Documents")
    folder2 = Folder("Pictures")
    root.add(folder1)
    root.add(folder2)

    file1 = File("report", "doc", 1024)
    file2 = File("family", "jpg", 2048)
    folder1.add(file1)
    folder2.add(file2)

    folder3 = Folder("Downloads")
    folder1.add(folder3)

    file3 = File("data", "csv", 512)
    folder3.add(file3)

    root.print_tree()
    print("\nLongest path:", root.get_longest_path())


if __name__ == "__main__":
    main()
