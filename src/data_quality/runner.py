from pyspark.sql import DataFrame


def run_checks(df: DataFrame, checks: list) -> list[dict]:
    """
    Execute a list of data quality checks and return their results.
    """

    results = []

    for check in checks:
        try:
            result = check(df)
            results.append(result)

        except Exception as e:
            results.append({
                "check": check.__name__,
                "status": "ERROR",
                "violations": None,
                "total_rows": None,
                "error": str(e)
            })

    return results