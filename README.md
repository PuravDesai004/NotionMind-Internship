# NotionMind internship: telehealth analytics

A collection of internship exercises culminating in a multi-agent system that analyzes a synthetic telehealth dataset and produces Markdown and HTML reports.

The Week 6 pipeline uses four agents to examine program performance, patient segments, retention, and anomalies. A coordinator combines their findings, and a Python report generator formats the result. The repository also retains the earlier weekly notebooks and experiments.

## Results

The bundled Week 6 example has 2,000 synthetic records. Count them from the repository root without calling an API:

```powershell
python -c "import csv; f=open('Week 6/telehealth.csv', encoding='utf-8-sig', newline=''); print(sum(1 for _ in csv.DictReader(f)))"
```

The Week 6 documentation reports an approximate end-to-end runtime, but it was not remeasured during this audit. No live Claude call was made.

## Flow and stack

`Week 6/agents_complete.py` coordinates the agents and pandas analysis tools. `Week 6/report_generator.py` formats their output. The implementation uses Python, pandas, the Anthropic API, and `python-dotenv`. See [Week 6/README.md](Week%206/README.md) for the original design notes and input schema.

## Quickstart

The record-count command above runs offline. The full pipeline requires an Anthropic API key and makes paid or rate-limited calls; it was not run as part of this audit. After obtaining approval for those calls, follow the setup in [Week 6/README.md](Week%206/README.md). Keep the key in an ignored `.env` file and do not commit it.

## Project structure

- `Week 1/` through `Week 5/`: notebooks and earlier iterations.
- `Week 6/`: the multi-agent pipeline, report generator, sample data, and documentation.

## Tests

There is no root automated test suite. The earlier notebooks contain examples and saved outputs. The report generator and full provider workflow have not been independently rerun here.

## Data and limitations

The included telehealth examples are synthetic, as confirmed by the project owner. The CSVs are example inputs for the internship exercises; the repository does not document a reproducible generator for every weekly CSV. The pipeline expects specific column names and its generated recommendations require human review. It is not validated for clinical decisions.

## License

No license file is supplied in this repository. The Week 6 documentation describes the work as an internal internship project; confirm the applicable rights before reuse.
