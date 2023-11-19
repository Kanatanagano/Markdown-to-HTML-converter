import sys
import markdown


def main():
    command = sys.argv[1]
    inputPath = sys.argv[2]
    outputPath = sys.argv[3]


    if command == "markdown":
        if inputPath.split(".")[-1] != "md" and inputPath.split(".")[-1] != "markdown" and outputPath.split(".")[-1] != "html" and len(sys.argv) != 4:
            with open(inputPath, "r") as file:
                text = file.read()
        else:
            print("Invalid file type")
        html = markdown.markdown(text,extensions=["toc", "codehilite", "sane_lists", "extra"])
        with open(outputPath, "w") as f:
            f.write(html)
    

if __name__ == "__main__":
    main()

    
