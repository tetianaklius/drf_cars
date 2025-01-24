from better_profanity import profanity

from apps.cars.adverts.models import CarAdvertModel


class ProfanityChecker:

    def check_profanity(self, data: dict):
        print(data)
        if data["profanity_edit_count"] > 4:
            return "Deactivate"
        if profanity.contains_profanity(data["title"]):  # True or False
            data["profanity_edit_count"] += 1
            return False
        if profanity.contains_profanity(data["description"]):  # True or False
            data["profanity_edit_count"] += 1
            return False
        return data
