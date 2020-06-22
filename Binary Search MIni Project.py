import time
from random import choice
from string import ascii_lowercase as letters


def binary_iter(num, arr):
    start = 0
    stop = len(arr)-1
    while start <= stop:
        mid = (start + stop) // 2
        if num == arr[mid]:
            return mid, f"{num} found at index: {mid}"
        elif num > arr[mid]:
            start = mid+1
        else:
            stop = mid-1
    return None, f"{num} not found in list."


def time_analyzer(func, *args):
    tic = time.time()
    func(*args)  # accept variable list of arguments.
    toc = time.time()
    seconds = toc - tic
    print(func.__name__.capitalize(), "\t-> Elapsed time:", round(seconds, 10))


# generate and get random emails

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))


def get_domain(list_of_domains):
    return choice(list_of_domains)


def generate_email(length_of_name, list_of_domains, total_emails):
    emails = []
    for i in range(total_emails):
        emails.append(generate_name(length_of_name)+"@"+get_domain(list_of_domains))
    return emails


# domain lists
list_of_domains = ["gmail.com", "yahoo.com", "minerva.kgi.edu"]

# generate emails and add dummy/test email to list of emails
emails = generate_email(8, list_of_domains, 1000000)
test_email = "philip.boakye@minerva.kgi.edu"
emails.append(test_email)

# sort list to be able to use binary search function
sorted_emails = sorted(emails)

# execute binary search to find test email in sorted emails and print result (including located index)
index, found = binary_iter(test_email, sorted_emails)
print(found)
if index:
    print("Element at index:", index, "is", sorted_emails[index])

# execute time analysis of functions
time_analyzer(binary_iter, test_email, sorted_emails)
time_analyzer(generate_email, 8, list_of_domains, 1000000)


