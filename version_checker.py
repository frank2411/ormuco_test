class NotValidVersionNumber(Exception):
    pass


class VersionChecker(object):

    def convert_version_to_float(self, version):
        version_start_number = version[0]

        # I delete the start number for later string formatting
        del version[0]

        if len(version) <= 1:
            return float(version_start_number)

        convertable_version = "{}.{}".format(version_start_number, ''.join(version))
        return float(convertable_version)

    def process_versions(self, version_1, version_2):
        self.version1 = version_1
        self.version2 = version_2

        try:
            version_1 = self.convert_version_to_float(version_1.split("."))
        except ValueError:
            raise NotValidVersionNumber("Invalid version number for first argument provided")

        try:
            version_2 = self.convert_version_to_float(version_2.split("."))
        except ValueError:
            raise NotValidVersionNumber("Invalid version number for second argument provided")

        greater_version = self.version1
        lesser_version = self.version2

        if version_1 == version_2:
            return self.EQUAL_PHRASE

        if version_1 < version_2:
            greater_version = self.version2
            lesser_version = self.version1

        return greater_version, lesser_version

    def get_greater(self, version_1, version_2):
        greater_version, lesser_version = self.process_versions(version_1, version_2)
        return greater_version

    def get_lesser(self, version_1, version_2):
        greater_version, lesser_version = self.process_versions(version_1, version_2)
        return lesser_version
