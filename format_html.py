if __name__ == "__main__":
    raw = open("resume.html").read()
    formatted = raw.replace("Work Experience", "Work Experience and Activities")\
        .replace("(expected)", "(exp)")

    f = open("resume.html", "w")
    f.write(formatted)
    f.close()
