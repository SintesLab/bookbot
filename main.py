def main():
    book_location = "books/frankenstein.txt"
    with open(book_location) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    char_count = count_chars(file_contents)
    print(f"--- Begin report of {book_location} ---")
    print(f"{word_count} words found in the document\n\n")
    print(report(char_count))
    print("--- End report ---")


def count_words(file_contents):
    word_counter = 0
    words = file_contents.split()
    for word in words:
        word_counter += 1
    return word_counter


def count_chars(file_contents):
    lowercase_contents = to_lowercase(file_contents)
    lowercase_set = to_set(lowercase_contents)
    char_count = dict.fromkeys(lowercase_set, 0)
    for item in lowercase_contents:
        if item in char_count:
            char_count[item] += 1
    return char_count


def to_set(lowercase):
    return set(lowercase)


def to_lowercase(contents):
    lowered_contents = contents.lower()
    return lowered_contents


def report(char_count):
    dict = {}
    for char in char_count:
        if char.isalpha():
            dict[char] = char_count[char]
    sorted_report = sort_report(dict)
    output_total = ""
    for element in sorted_report:
        output_dict = element
        output_single = f"The '{output_dict["letter"]}' character was found {output_dict["count"]} times"
        if output_total == "":
            output_total = output_single
        output_total = output_total + "\n" + output_single
    return output_total


def sort_report(to_sort):
    sorted_report = []
    for element in to_sort:
        dict = {}
        dict["letter"] = element
        dict["count"] = to_sort[element]
        sorted_report.append(dict)
    sorted_report.sort(reverse=False, key=sort_report_helper)
    return sorted_report


def sort_report_helper(dict):
    return dict["letter"]


main()
