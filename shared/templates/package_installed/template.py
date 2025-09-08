import re


def preprocess(data, lang):
    if "evr" in data:
        evr = data["evr"]
        # Check if EVR is in the correct format (with or without epoch)
        if evr:
            # If EVR doesn't have an epoch but matches version-release format
            if not re.match(r"\d:", evr, 0) and re.match(
                r"\d[\d\w+.]*-\d[\d\w+.]*", evr, 0
            ):
                # Print notification about epoch-less string
                print(
                    f"Warning: EVR string '{evr}' for package '{data['pkgname']}' is missing an epoch"
                )
            # Validate the format - allowing both with and without epoch
            elif not (
                re.match(r"\d:\d[\d\w+.]*-\d[\d\w+.]*", evr, 0)
                or re.match(r"\d[\d\w+.]*-\d[\d\w+.]*", evr, 0)
            ):
                raise RuntimeError(
                    "ERROR: input violation: evr key should be in "
                    "epoch:version-release or version-release format, but package {0} has set "
                    "evr to {1}".format(data["pkgname"], evr)
                )
    return data
