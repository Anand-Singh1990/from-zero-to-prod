from prefect import flow, task
import logging

logger = logging.getLogger()


@task
def validate_numbers(numbers: list[int]) -> list[int]:
    if not numbers:
        raise ValueError("Numbers list cannot be empty")
    logger.info(f"Validated numbers: {numbers}")
    return numbers


@task
def calculate_stats(numbers: list[int]) -> dict:
    result = {
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers) / len(numbers),
        "max": max(numbers),
    }
    logger.info(f"Calculated stats: {result}")
    return result


@flow(name="simple-stats-flow")
def stats_flow(numbers: list[int]) -> dict:
    validated = validate_numbers(numbers)
    stats = calculate_stats(validated)
    return stats
