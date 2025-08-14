from importlib.metadata import version

class LibVersion:
    """Class to retrieve the version of a library."""

    @staticmethod
    def get_version(lib_name):
        """Returns the version of the specified library."""
        try:
            return version(lib_name)
        except Exception as e:
            return f"Error retrieving version for {lib_name}: {e}"


if __name__ == "__main__":
    # Example usage
    print("Pandas version:", LibVersion.get_version("pandas"))
