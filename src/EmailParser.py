class EmailParser:
    @staticmethod
    def is_student(email):
        return "student.pxl.be" in email

    @staticmethod
    def is_teacher(email):
        return not EmailParser.is_student(email) and "pxl.be" in email

    @staticmethod
    def is_valid(email):
        return EmailParser.is_student(email) or EmailParser.is_teacher(email)

    @staticmethod
    def get_name_from_email(email):
        return email.split("@")[0].strip(".")

    @staticmethod
    def get_filename_from_email(email):
        return f"{EmailParser.get_name_from_email(email)}.csv"
