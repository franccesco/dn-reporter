import time
import requests
from IPython.core.ultratb import AutoFormattedTB


class DNReporter:
    """Report Deepnote's project status to Slack"""

    def __init__(self, endpoint_url, report_name, project_url=None, auto_override=True):
        self.endpoint_url = endpoint_url
        self.report_name = report_name
        self.project_url = project_url
        self.start_time = time.time()
        itb = AutoFormattedTB(mode="Plain", tb_offset=1)
        if auto_override:
            self.override_failure()

    def execution_time(self):
        execution_time = round(time.time() - self.start_time, 2)
        return execution_time

    def report_status(self, status, execution_time=None):
        if execution_time is None:
            execution_time = self.execution_time()
        req_data = {
            "name": self.report_name,
            "url": self.project_url if self.project_url else "Not Provided",
            "execution_time": str(execution_time),
            "status": status,
        }
        response = requests.post(self.endpoint_url, json=req_data)
        print(f"📣 Project {status}; report was sent to Slack.")

    def custom_exc(self, shell, etype, evalue, tb, tb_offset=None):
        execution_time = self.execution_time()
        shell.showtraceback((etype, evalue, tb), tb_offset=tb_offset)
        self.report_status("Failed")

    def report_success(self):
        self.report_status("Successful")

    def override_failure(self):
        return get_ipython().set_custom_exc((Exception,), self.custom_exc)
