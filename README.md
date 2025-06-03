# ETL Automation Python Library

This library provides an ETL automation framework with generic pipeline classes, extraction sources, scheduling, monitoring, alerting, and reporting.

## Installation

```bash
pip install .
```

## Usage

- Implement custom pipeline by extending `Pipeline` and overriding `transform`.
- Use `ExtractionSourceFactory` to create extraction sources.
- Configure and start the scheduler, monitoring, and reporting services.