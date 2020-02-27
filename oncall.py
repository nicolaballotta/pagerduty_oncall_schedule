import os
import requests
import json


class PagerdutyClient:
    def __init__(self, token):
        self.pagerduty_token = token

    @staticmethod
    def _url():
        return 'https://api.pagerduty.com/'

    def call_api(self, resource_path, params=None):
        headers = {
            'Accept': 'application/vnd.pagerduty+json;version=2',
            'Authorization': 'Token token={token}'.format(token=self.pagerduty_token)
        }
        url = self._url() + resource_path
        response_data = requests.get(url, headers=headers, params=params)
        return json.loads(response_data.text)

    def get_oncall(self, schedule_id):
        payload = {
            'schedule_ids[]': schedule_id
        }
        response = self.call_api('oncalls', params=payload)
        on_call = response['oncalls'][0]['user']['summary']
        return on_call


if __name__ == '__main__':
    pd = PagerdutyClient(os.getenv('PD_TOKEN'))
    print(80 * "-")
    print('The on call winner is: {}').format(pd.get_oncall(os.getenv('SCHEDULE')))
    print(80 * "-")
