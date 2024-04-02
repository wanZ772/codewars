def find_needle(haystack):
    # with index function
    # return "found the needle at position " + str(haystack.index("needle"))

    # withput index function
    for i in range(len(haystack) - 1):
        if haystack[i] == "needle":
            return f"found the needle at position {i}"
print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] ))