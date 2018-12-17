class NotValidVersionNumber(Exception):
    pass


class VersionChecker(object):

    def __init__(self, *args, **kwargs):
        self.GREATER_THAN_PHRASE = "{} is greater than {}"
        self.LESSER_THAN_PHRASE = "{} is lesser than {}"
        self.EQUAL_PHRASE = "Versions are equal"

    def convert_version_to_float(self, version):
        version_start_number = version[0]
        convertable_version = "{}.{}".format(version_start_number, ''.join(version))
        return float(convertable_version)

    def process_versions(self, version_1, version_2, do_simple_check=False):
        self.version1 = version_1
        self.version2 = version_2

        try:
            version_1 = self.convert_version_to_float(version_1.split("."))
        except ValueError:
            raise NotValidVersionNumber("Invalid version number for first argument provided") from None

        try:
            version_2 = self.convert_version_to_float(version_2.split("."))
        except ValueError:
            raise NotValidVersionNumber("Invalid version number for second argument provided") from None

        greater_version = self.version1
        lesser_version = self.version2

        if version_1 == version_2:
            return None, None, True

        if do_simple_check:
            return version_1, version_2, False

        if version_1 < version_2:
            greater_version = self.version2
            lesser_version = self.version1

        return greater_version, lesser_version, False

    def get_greater(self, version_1, version_2):
        greater_version, lesser_version, equal = self.process_versions(version_1, version_2)
        return greater_version

    def get_lesser(self, version_1, version_2):
        greater_version, lesser_version, equal = self.process_versions(version_1, version_2)
        return lesser_version

    def get_greater_and_lesser(self, version_1, version_2):
        greater_version, lesser_version, equal = self.process_versions(version_1, version_2)
        return greater_version, lesser_version

    def compare_versions(self, version_1, version_2):
        """
            For this simple check I don't need to reorder the versions for the check.
            I'll do the check later for a more versatile and a first argument based output.
            This method has a Human phrase-like respose.
        """

        first_version, second_version, equal = self.process_versions(version_1, version_2, do_simple_check=True)

        if equal:
            return self.EQUAL_PHRASE

        if first_version > second_version:
            return self.GREATER_THAN_PHRASE.format(version_1, version_2)
        else:
            return self.LESSER_THAN_PHRASE.format(version_1, version_2)
