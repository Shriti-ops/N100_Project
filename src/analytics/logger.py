import logging
import os

os.makedirs("output", exist_ok=True)

logging.basicConfig(
    filename="output/ratio_edge_cases.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


def log_edge_case(
    company_id,
    year,
    ratio,
    issue,
    category
):
    """
    Log ratio anomalies
    """

    logging.info(
        f"Company={company_id} | "
        f"Year={year} | "
        f"Ratio={ratio} | "
        f"Issue={issue} | "
        f"Category={category}"
    )