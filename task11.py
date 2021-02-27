name = input("Enter full name ")
tag_h1 = [" <h1>", name, "</h1>"]
characteristics = input("Describe yourself in a few words ")
tag_hr = [" <hr>", characteristics, "</hr>"]
with open("webpage.html", "w") as file:
    file.write("<html>" + "\n")
    file.write("<head>" + "\n")
    file.write("</head>" + "\n")
    file.write("<body>" + "\n")
    file.write(" <center>" + "\n")
    for element in tag_h1:
        file.write(element + '\n')
    file.write(" </center>" + "\n")
    for element in tag_hr:
        file.write(element + '\n')
    file.write("</body>" + "\n")
    file.write("</html>" + "\n")
file.close()


