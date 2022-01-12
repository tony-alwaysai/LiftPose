
"""
Tracks current key_point coordinates and uses these to check for
various improper postures.
Stores a scale factor, which is used to reduce or increase the distances
that are used to calculate distance between key_points to determine if
improper posture is detected.
Posture is measured with these individual functions in order to allow users to
check for specific bad behavior,
"""
class CheckPosture:

    def __init__(self, scale=1, key_points={}):
        self.key_points = key_points
        self.scale = scale
        self.message = ""

    def set_key_points(self, key_points):
        """
        Updates the key_points dictionary used in posture calculations
        :param key_points: {}
            the dictionary to use for key_points
        """
        self.key_points = key_points

    def get_key_points(self):
        """
        Returns the instance's current version of the key_points dictionary
        :return: {}
            the current key_points dictionary
        """
        return self.key_points

    def set_message(self, message):
        """
        Setter to update the message manually if needed
        :param message: string
            The message to override the current message
        """
        self.message = message

    def build_message(self):
        """
        Builds a string with advice to the user on how to correct their posture
        :return: string
            The string containing specific advice
        """
        bent = self.knees_bent()
        current_message = ""
        if not bent:
            current_message += f"Bend your knees\n"
        if bent:
            current_message += f""

        self.message = current_message
        return current_message

    def get_message(self):
        """
        Getter method to return the current message
        :return: string
            The current posture message
        """
        return self.message

    def set_scale(self, scale):
        """
        Sets the scale factor to use for the posture calculations
        :param scale: int
            The value to scale the measurements used in the calculations by. Larger values will
            mean a less stringent calculation.
        """
        self.scale = scale

    def get_scale(self):
        """
        Returns the current scale for the instance
        :return: int
            The scale being used by the instance for posture calculations
        """
        return self.scale


    def knees_bent(self):
        if self.key_points['Right Shoulder'].x != -1 and self.key_points['Right Knee'].x != -1 and self.key_points['Right Hip'].x != -1 and int(self.key_points['Right Shoulder'].x) in range(int(self.key_points['Right Hip'].x + (self.scale * 30)), int(self.key_points['Right Hip'].x + (self.scale * 500))) and int(self.key_points['Right Knee'].x) in range(int(self.key_points['Right Hip'].x),int(self.key_points['Right Hip'].x + (self.scale * 75))):
            return (False,int(self.key_points['Right Shoulder'].x),int(self.key_points['Right Hip'].x),int(self.key_points['Right Knee'].x))
        return (True,int(self.key_points['Right Shoulder'].x),int(self.key_points['Right Hip'].x),int(self.key_points['Right Knee'].x))


    def correct_posture(self):
        """
        Checks all current posture functions
        :return: Boolean
            True if all posture functions return True; False otherwise
        """
        return all([self.knees_bent()])

