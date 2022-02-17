# Blacklist Mailserver Check

This tool produced for checking if your mail servers blacklisted by any blacklist authorities. To achieve this it is using python3 and MXtoolbox REST API. This tool also can use other functions documented in API such as lookup and usage.

## Simple Usage

One of the two arguments is required for tool to run "-a" or "-l"
For raw output use "-r"
```
git clone https://github.com/the-src/blacklist_mailservers.git && cd blacklist_mailservers
python3 mxtoolbox.py -a [action] -l [lookup_type] -r
```

## Output

```
┌──(root🐧 kali)-[/opt/blacklist_check]
└─# python3 mxtoolbox.py -r -l txt
What do you want to lookup?
>> google.com
{
  "UID": null,
  "ArgumentType": "domain",
  "Command": "txt",
  "IsTransitioned": false,
  "CommandArgument": "google.com",
  "TimeRecorded": "2022-02-17T03:46:13.079517-06:00",
  "ReportingNameServer": "ns1.google.com",
  "TimeToComplete": "30",
  "RelatedIP": null,
  "ResourceRecordType": 16,
  "IsEmptySubDomain": false,
  "IsEndpoint": false,
  "HasSubscriptions": false,
  "AlertgroupSubscriptionId": null,
  "Failed": [],
  "Warnings": [],
  "Passed": [
    {
      "ID": 506,
      "Name": "DNS Record Published",
      "Info": "DNS Record found",
      "Url": "https://mxtoolbox.com/Problem/txt/DNS-Record-Published?page=prob_txt&showlogin=1&hidetoc=1&action=txt:google.com",
      "PublicDescription": null,
      "IsExcludedByUser": false
    }
  ],
```

For questions [email](mailto:southrain@softsec.xyz) me
