
# DN-Reporter

This is a small package that is used to identify errors in Deepnote / Jupyter notebooks without having to wrap your code in a `try/else` statement.

The error can happen in any cell, and it will notify the data science team via Slack (or any HTTP endpoint).


## Installation

To install it you will need your user token and then install the package from the repository directly.

```
pip install https://github.com/franccesco/dn-reporter@main
```

## Usage/Examples

Once the package is installed, you can create a new Deepnote project and then initialize the `DNReporter` class and pass an endpoint URL and your Deepnote project name:

```python
from dnreporter import DNReporter

reporter = DNReporter('https://endpoint.com', 'report_name', 'project_url')
```

The initialization process will automatically override the usual halt process when an exception is encountered in any cell. If you want to disable the automatic override you can pass the `auto_override=False` argument, and then initialize it yourself:

```python
reporter = DNReporter('endpoint_url', 'report_name', auto_override=False)
reporter.override_failure()
```

At the end of the notebook, you can use the method `.report_sucess()` to send a message to Slack reporting that the project was successfully executed:

```python
reporter.report_success()
```
