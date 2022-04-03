class TransactionTypes:
    TABLE_NAME = "transaction_types"
    COLUMN_TRANSACTION_TYPES_CODE = "transaction_type_code"
    COLUMN_TRANSACTION_TYPES_DESCRIPTION = "transaction_types_description"

    @classmethod
    def getCreateQuery(cls) -> str:
        return (f"CREATE TABLE IF NOT EXISTS {cls.TABLE_NAME}("
                f"{cls.COLUMN_TRANSACTION_TYPES_CODE} INT(10) PRIMARY KEY ,"
                f"{cls.COLUMN_TRANSACTION_TYPES_DESCRIPTION} VARCHAR(40));")
