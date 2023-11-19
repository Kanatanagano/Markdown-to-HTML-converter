import sys
import markdown


def main():
    command = sys.argv[1]
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]


    if command == "markdown":
        try:
            with open(inputPath, "r") as file:
                text = file.read()
        except FileExistsError:
            print("Invalid file type")
        html = markdown.markdown(text,extensions=["toc", "codehilite", "sane_lists", "extra"])
        with open(outputPath, "w") as f:
            f.write(html)
    

if __name__ == "__main__":
    main()

    
