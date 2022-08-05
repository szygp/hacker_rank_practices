def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split('@')
        website, extension = url.split('.')
    except ValueError:
        return False
    if username.replace('_', '').replace('-','').isalnum() is False:
        return False
    elif website.isalnum() is False:
        return False
    elif extension.isalpha is False:
        return False
    elif len(extension)>3:
        return False
    else:
        return s

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)