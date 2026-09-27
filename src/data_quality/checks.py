from pyspark.sql import DataFrame


def check_not_null(df: DataFrame, column: str) -> dict:
    """Check whether a column contains null values."""

    total_rows = df.count()
    null_rows = df.filter(df[column].isNull()).count()

    return {
        "check": f"{column}_not_null",
        "status": "PASS" if null_rows == 0 else "FAIL",
        "violations": null_rows,
        "total_rows": total_rows
    }


def check_unique(df: DataFrame, columns: list[str]) -> dict:
    """Check whether a column or combination of columns is unique."""

    total_rows = df.count()
    unique_rows = df.select(*columns).distinct().count()
    duplicate_rows = total_rows - unique_rows

    return {
        "check": f"{'_'.join(columns)}_unique",
        "status": "PASS" if duplicate_rows == 0 else "FAIL",
        "violations": duplicate_rows,
        "total_rows": total_rows
    }


def check_accepted_values(
    df: DataFrame,
    column: str,
    accepted_values: list
) -> dict:
    """Check whether all values belong to an accepted set."""

    invalid_rows = df.filter(
        ~df[column].isin(accepted_values)
    ).count()

    total_rows = df.count()

    return {
        "check": f"{column}_accepted_values",
        "status": "PASS" if invalid_rows == 0 else "FAIL",
        "violations": invalid_rows,
        "total_rows": total_rows
    }


def check_non_negative(df: DataFrame, column: str) -> dict:
    """Check whether a numeric column contains negative values."""

    invalid_rows = df.filter(
        df[column] < 0
    ).count()

    total_rows = df.count()

    return {
        "check": f"{column}_non_negative",
        "status": "PASS" if invalid_rows == 0 else "FAIL",
        "violations": invalid_rows,
        "total_rows": total_rows
    }


def check_range(
    df: DataFrame,
    column: str,
    min_value,
    max_value
) -> dict:
    """Check whether values are within a specified range."""

    invalid_rows = df.filter(
        (df[column] < min_value) |
        (df[column] > max_value)
    ).count()

    total_rows = df.count()

    return {
        "check": f"{column}_range",
        "status": "PASS" if invalid_rows == 0 else "FAIL",
        "violations": invalid_rows,
        "total_rows": total_rows
    }