from better_profanity import profanity


class ProfanityChecker(object):

    def check_profanity(self, data: dict):
        if profanity.contains_profanity(data["title"]):  # True or False
            return False
        if profanity.contains_profanity(data["description"]):  # True or False
            return False
        return data
