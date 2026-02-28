def https_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not Found"
        case 500:
            return "Case not found"
        case _:
            return "Unkonown status"
        
print(https_status(600))