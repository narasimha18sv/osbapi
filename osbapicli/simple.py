import logging
import requests
import json
from cliff.command import Command
import argparse

class ParseKwargs(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        setattr(namespace, self.dest, dict())
        for value in values:
            key, value = value.split('=')
            getattr(namespace, self.dest)[key] = value

class Catalog(Command):
    "Lists all the catalog items in a service broker"

    log = logging.getLogger(__name__)

    def take_action(self, parsed_args):
        try: 
            headers={'X-Broker-API-Version': '2.16', 'Content-Type': 'application/json'}
            response=requests.get("http://127.0.0.1:5000/v2/catalog", headers=headers)
            print(response.json())
        except Exception as e:
            print(e)


class Provision(Command):
    "Provision services"

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(Provision, self).get_parser(prog_name)
        parser.add_argument('--service_id')
        parser.add_argument('--plan_id')
        parser.add_argument('--parameters', nargs='*', action=ParseKwargs)

        return parser

    def take_action(self, parsed_args):
        service_id=parsed_args.service_id
        plan_id=parsed_args.plan_id
        parameters=parsed_args.parameters
        body={'service_id': service_id, 'plan_id': plan_id, 'parameters': parameters, 'organization_guid': 'testing', 'space_guid': 'testing'}
        request_id='wf-osbapi-001'
        headers={'X-Broker-API-Version': '2.16', 'Content-Type': 'application/json'}
        response=requests.put("http://127.0.0.1:5000/v2/service_instances/"+request_id, headers=headers, data=json.dumps(body))
        print(f'Response code {response}, request_id: {request_id}')
        print(response.json())


class DeProvision(Command):
    "DeProvision services"

    log = logging.getLogger(__name__)
    
    def get_parser(self, prog_name):
        parser = super(DeProvision, self).get_parser(prog_name)
        parser.add_argument('--service_id')
        parser.add_argument('--plan_id')
        parser.add_argument('--request_id')
        return parser

    def take_action(self, parsed_args):
        service_id=parsed_args.service_id
        plan_id=parsed_args.plan_id
        request_id=parsed_args.request_id
        headers={'X-Broker-API-Version': '2.16', 'Content-Type': 'application/json'}
        response=requests.delete("http://127.0.0.1:5000/v2/service_instances/"+request_id+"?service_id="+service_id+"&plan_id="+plan_id, headers=headers)
        print(f'Response code {response.status_code}, request_id {request_id} deprovisioned')
   

        
