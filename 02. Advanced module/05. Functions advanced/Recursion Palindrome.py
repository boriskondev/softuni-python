def palindrome(string_to_check, index):
    end_index = -1 + index * - 1
    if string_to_check[index] == string_to_check[end_index]:
        if index == ((end_index * -1) - 1):
            return f"{string_to_check} is a palindrome"
        index += 1
        return palindrome(string_to_check, index)
    return f"{string_to_check} is not a palindrome"


print(palindrome("neven", 0))