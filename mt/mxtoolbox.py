from email import message
import json
import pytz
import datetime
import requests as r
from tomlkit import key

BASEURL = 'https://api.mxtoolbox.com/api/v1'
TIME = pytz.timezone('Turkey')  # Change here if your zone is different


class mxtoolbox:

    def __init__(self, key):
        self.key = key

    def lookup(self, command, argument, RAW=False):
        self.command = command
        self.argument = argument
        URL = BASEURL + f'/Lookup/{command}/?argument={argument}'
        resp = r.get(URL, headers={'Authorization': self.key})
        respjson = json.loads(resp.text)

        if RAW:
            return resp.text
        else:
            try:
                if command == 'a':
                    return "'\033[1m" + respjson["ReportingNameServer"] + "\033[0m' reported that " + respjson["CommandArgument"] + " belongs to '\033[1m" + respjson["Information"][0]["IP Address"] + "\033[0m' IP address and '\033[1m" + respjson["Information"][0]["Domain Name"] + "\033[0m' domain name."
                elif command == 'cname':
                    return "'\033[1m" + respjson["ReportingNameServer"] + "\033[0m' reported that " + respjson["CommandArgument"] + " have a cname points to " + respjson["Information"][0]["Canonical Name"]
                elif command == 'mx':
                    mxlist = list(enumerate(respjson["Information"]))
                    count = 0
                    message = "\033[1m" + respjson["ReportingNameServer"] + \
                        "\033[0m reported that "
                    for e in mxlist:
                        message += "\033[1m[" + e[1]['Hostname'] + \
                            ":" + e[1]['IP Address'] + "\033[0m]"
                        count += 1
                    message += " is/are mail servers for \033[1m" + \
                        respjson["CommandArgument"]
                    return message
                else:
                    return "Command not built, use raw."
            except:
                return "An error occurred."

    def monitor(self, RAW=False, muid=0):
        URL = BASEURL + '/Monitor'

        if muid:
            URL = BASEURL + f'/Monitor/{muid}'

        resp = r.get(URL, headers={'Authorization': self.key})
        respjson = json.loads(resp.text)

        if RAW:
            return resp.text
        else:
            if respjson[0]["StatusSummary"] == "Not Blacklisted":
                # This return statement is also customizable.
                return datetime.datetime.now(TIME).strftime("[%H:%M:%S - %d/%m/%Y] ") + respjson[0]["Name"].split(':')[1] + " is not blacklisted."
            else:
                for blist in respjson[0]["Failing"]:
                    return datetime.datetime.now(TIME).strftime("[%H:%M:%S - %d/%m/%Y] ") + respjson[0]["Action"]["Address"] + " is blacklisted by '\033[1m" + blist["Name"] + "\033[0m'\nFor delisting please follow the URL: \n\033[1m" + blist["DelistUrl"]

    def usage(self, RAW=False):

        URL = BASEURL + '/Usage'
        resp = r.get(URL, headers={'Authorization': self.key})
        respjson = json.loads(resp.text)

        if RAW:
            return resp.text
        else:
            return datetime.datetime.now(TIME).strftime("[%H:%M:%S - %d/%m/%Y] ") + str(respjson["DnsRequests"]) + " queries made. Remaining: " + str(int(respjson["DnsMax"]) - int(respjson["DnsRequests"]))
