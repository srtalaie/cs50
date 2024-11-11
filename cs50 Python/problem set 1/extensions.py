user_input = input("File Name: ")

# Sanitize user input and make lowercase
user_input = user_input.strip().lower()

# Separate string by '.' to get the file type that trails after the '.'
user_input_arr = user_input.rsplit(".", 1)
file_extension = user_input_arr[-1]


def file_ext_checker(file_ext):
    match file_ext:
        case "gif":
            return "image/gif"
        case "jpg":
            return "image/jpeg"
        case "jpeg":
            return "image/jpeg"
        case "png":
            return "image/png"
        case "pdf":
            return "application/pdf"
        case "txt":
            return "text/plain"
        case "zip":
            return "application/zip"
        case _:
            return "application/octet-stream"


print(file_ext_checker(file_extension))
