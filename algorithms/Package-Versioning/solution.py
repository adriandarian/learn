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
