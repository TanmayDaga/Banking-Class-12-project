class AccountType:
    """static class for holding constants for AccountTypes table"""

    TABLE_NAME = "account_types"
    COLUMN_ACCOUNT_TYPES_CODE = "account_types_code"
    COLUMN_ACCOUNT_TYPES_DESCRIPTION = "account_types_description"

    @classmethod
    def getCreateQuery(cls) -> str:
        return (f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}("
                f"{cls.COLUMN_ACCOUNT_TYPES_CODE} INT(10) PRIMARY KEY,"
                f"{cls.COLUMN_ACCOUNT_TYPES_DESCRIPTION} VARCHAR(40));")
