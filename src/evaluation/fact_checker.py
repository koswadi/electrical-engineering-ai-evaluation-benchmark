"""
Electrical Engineering Fact Checker
"""

class FactChecker:

    FACT_RULES = {

        "efficiency above 100":
        False,

        "power factor greater than 1":
        False,

        "frequency indonesia 60 hz":
        False,

        "frequency indonesia 50 hz":
        True
    }

    def check(
        self,
        answer
    ):

        answer = answer.lower()

        for fact, validity in self.FACT_RULES.items():

            if fact in answer:

                return "Pass" if validity else "Fail"

        return "Pass"


if __name__ == "__main__":

    checker = FactChecker()

    print(
        checker.check(
            "Power factor greater than 1"
        )
    )