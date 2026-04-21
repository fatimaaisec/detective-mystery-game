class Suspect:
    def __init__(self, name, occupation, alibi, is_criminal=False, motive=""):
        self.name = name
        self.occupation = occupation
        self.alibi = alibi
        self.is_criminal = is_criminal
        self.motive = motive
    
    def interview(self):
        """Return suspect's interview response"""
        return f"Alibi: {self.alibi}"


def get_all_suspects():
    """Return list of all suspects"""
    suspects = [
        Suspect(
            name="Professor Morgan",
            occupation="Jewel Expert",
            alibi="I was in my office studying the diamond's specifications. I had nothing to do with the theft!",
            is_criminal=True,
            motive="Needed money for secret gambling debts. The diamond was worth millions."
        ),
        Suspect(
            name="James Wilson",
            occupation="Security Guard",
            alibi="I was on patrol all night. I checked all the locks and everything was secure.",
            is_criminal=False
        ),
        Suspect(
            name="Sarah Chen",
            occupation="Jeweler",
            alibi="I was at home with my family. We had dinner together. They can confirm it.",
            is_criminal=False
        ),
        Suspect(
            name="Marcus Stone",
            occupation="Wealthy Collector",
            alibi="I was attending a private party at my mansion. Many witnesses saw me there.",
            is_criminal=False
        ),
        Suspect(
            name="Lisa Turner",
            occupation="Cleaner",
            alibi="I was cleaning the east wing. I saw nothing unusual that night.",
            is_criminal=False
        )
    ]
    return suspects
