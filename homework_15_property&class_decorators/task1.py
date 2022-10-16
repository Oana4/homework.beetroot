import re


class CheckEmail:

    def __init__(self, email):
        if not CheckEmail.validate(email):
            raise ValueError("This email address it's not valid.")
        self.email = email

    @staticmethod
    def validate(email):
        valid_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.fullmatch(valid_email, email)


my_email = CheckEmail("sirbu.oana@gmail.com")
other_email = CheckEmail("absfc.com")
another_email = CheckEmail("universe@discover-you.com")
# the code returns an error because absfc.com is not a valid email address, and therefore
# we can't have an object with this attribute







