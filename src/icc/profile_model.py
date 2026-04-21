"""
profile_model.py

High-level representation of an ICC profile.
"""

class ICCProfile:
    """
    Represents parsed ICC profile metadata.
    """

    def __init__(self):

        self.size = None
        self.device_class = None
        self.color_space = None
        self.pcs = None
        self.creation_date = None

        self.tags = {}

    def add_tag(self, signature, data):
        self.tags[signature] = data

    def __repr__(self):
        return (
            f"<ICCProfile "
            f"class={self.device_class}, "
            f"space={self.color_space}, "
            f"pcs={self.pcs}, "
            f"tags={len(self.tags)}>"
        )