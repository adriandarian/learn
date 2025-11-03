#
# Package versioning
#
# Given strings older and newer, each representing software package versions in the format major.minor.patch, return whether the newer version is actually newer than the older.
#
# Example 1
#
# Input:
# older = "11.1.2"
# newer = "11.1.3"
#
# Output:
# True
#
# Explanation:
# The patch version of the `new` string is more recent.
#
# Example 2
#
# Input:
# older = "3.1.2"
# newer = "1.1.3"
#
# Output:
# False
#
# Explanation:
# The old version has a newer major version since 3 > 1
#
# Example 3
#
# Input:
# older = "3.1.2"
# newer = "3.2.3"
#
# Output:
# True
#
# Explanation:
# The minor version of the new package is more recent
#
# Example 4
#
# Input:
# older = "13.1.2"
# newer = "3.2.3"
#
# Output:
# False
#
# Explanation:
# Old version has a newer major version since 13 > 3
#

class Solution:
    def solve(self, older, newer):
        older = older.split(".")
        newer = newer.split(".")

        print(older)
        print(newer)

        if int(newer[0]) >= int(older[0]):
            if int(newer[1]) == 0:
                return True
            elif int(newer[1]) >= int(older[1]):
                if int(newer[2]) == 0:
                    return True
                elif int(newer[2]) > int(older[2]):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
