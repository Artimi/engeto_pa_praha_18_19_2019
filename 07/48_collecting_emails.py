my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''


def is_email(word):
    return '@' in word


def collect_emails(text):
    emails = []
    for word in text.split():
        if is_email(word):
            emails.append(word)
    return emails


def get_domains(emails):
    domains = []
    for email in emails:
        domain = email.split('@')[1]
        domains.append(domain)
    return domains


def has_digits(word):
    return any([char.isdigit() for char in word])


def get_numeric_emails(emails):
    numeric_emails = []
    for email in emails:
        if has_digits(email):
            numeric_emails.append(email)
    return numeric_emails


emails = collect_emails(my_str)
result = {
    'domains': get_domains(emails),
    'emails_with_nums': get_numeric_emails(emails),
}

print(result)
