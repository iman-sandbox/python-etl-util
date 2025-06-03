from setuptools import setup, find_packages

setup(
    name="etl_automation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "apscheduler",
    ],
    python_requires=">=3.8",
    author="Generated",
    description="ETL Automation library in Python",
)