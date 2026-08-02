"""
Gen-AI Insights Generator
--------------------------
Takes summary statistics from the EDA script (as a dict) and uses an LLM
(OpenAI API) to generate a natural-language executive summary of the
key trends found in the travel/hotel booking dataset.

Usage:
    from genai_insights import generate_insight_report
    report = generate_insight_report(summary_stats)
    print(report)
"""

import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

PROMPT_TEMPLATE = """
You are a travel industry data analyst assistant. Given the following
summary statistics from a travel/hotel booking dataset, write a concise,
plain-English executive summary (5-7 bullet points) highlighting the most
important trends, anomalies, and business-relevant takeaways -- including
any pricing or seasonality recommendations.

Summary statistics:
{stats}

Executive Summary:
"""


def generate_insight_report(summary_stats: dict) -> str:
    prompt = PROMPT_TEMPLATE.format(stats=summary_stats)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    example_stats = {
        "avg_price": 8500,
        "busiest_month": "December",
        "avg_lead_time_days": 21,
        "cancellation_rate": 0.08,
        "total_bookings": 15234,
    }
    print(generate_insight_report(example_stats))
