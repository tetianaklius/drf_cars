from better_profanity import profanity


class ProfanityChecker:

    def check_profanity(self, data: dict):
        # if profanity.contains_profanity(data["title"]):
        #     return False
        # if profanity.contains_profanity(data["description"]):
        #     return False

        if profanity.contains_profanity(data["title"]):
            return False
        if profanity.contains_profanity(data["text"]):
            return False

        return data
