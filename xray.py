import time
import requests
import json
from io import BytesIO
from zipfile import ZipFile

auth_json = {"client_id": "your_client_id",
             "client_secret": "your_secret_client_id"}


def get_test_plan(key):
    try:
        token = requests.post("https://xray.cloud.getxray.app/api/v2/authenticate", auth_json)
        token.raise_for_status()
        head = {"Authorization": "Bearer " + token.text[1:-1]}

        response = requests.get(f"https://xray.cloud.getxray.app/api/v2/export/cucumber?keys={key}", headers=head)
        response.raise_for_status()

        with ZipFile(BytesIO(response.content), 'r') as arch:
            files = []
            for file_name in arch.namelist():
                files.append(arch.read(file_name).decode('UTF-8'))
            return files


    except Exception as e:
        print(e)


def send_test_result(result):
    try:
        token = requests.post("https://xray.cloud.getxray.app/api/v2/authenticate", auth_json)
        token.raise_for_status()
        head = {"Content-Type": "application/json", "Authorization": "Bearer " + token.text[1:-1]}

        response = requests.post("https://xray.cloud.getxray.app/api/v2/import/execution", json=result, headers=head)
        response.raise_for_status()

        return json.loads(response.content.decode('utf-8'))["key"]

    except Exception as e:
        print(e)


def parse_test_plan(data):
    output = {}

    for file in data:
        for line in file.splitlines():
            if line.startswith("\t@TEST"):
                last_key = line.strip().split(" ", 1)[0][6:]
            if line.startswith("\t\t"):
                output[last_key] = line.strip()

    return output


def load_xray(key):
    test_plan = get_test_plan(key)
    time.sleep(1)

    if test_plan is not None:
        return parse_test_plan(test_plan)


if __name__ == "__main__":
    issue = input("Enter a Issue: ")
    load_xray(issue)
