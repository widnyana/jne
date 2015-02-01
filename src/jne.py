#!/usr/bin/env python
import json
import locale
locale.setlocale(locale.LC_NUMERIC, '')
import random
import requests
from tabulate import tabulate

from src.constant import *
from src.ua import user_agent


def __pretty_print(content):
    """Pretty print json"""
    print json.dumps(json.loads(content), indent=2, sort_keys=True)


def get_from_code(city):
    url = URL_CITY_FROM % city
    print "Querying Location code for: {}.\n".format(city)
    fetch = requests.get(url)

    if fetch.status_code == 200:

        stack = []
        headers = ['Code', 'Address']
        data = json.loads(fetch.content)
        for item in data:
            stack.append(list((
                item.get('code'),
                item.get('label')
            )))

        print tabulate(stack, headers)
    else:
        print "JNE server is malformed."


def get_target_code(city):
    url = URL_CITY_TO % city
    print "Querying Location code for: {}.\n".format(city)

    fetch = requests.get(url)
    if fetch.status_code == 200:

        stack = []
        headers = ['Code', 'Address']
        data = json.loads(fetch.content)
        for item in data:
            stack.append(list((
                item.get('code'),
                item.get('label')
            )))

        print tabulate(stack, headers)

    else:
        print "JNE server is malformed."


def checktariff(city_from=None, city_to=None, weight=None):
    payload = USERKEY
    request = {
        "from": city_from,
        "thru": city_to,
        "weight": weight
    }
    payload.update(request)

    ua = random.choice(user_agent)
    fetch = requests.post(URL_TARIFF, data=payload, headers={
        'User-Agent': ua
    })

    if fetch.status_code == 200:
        data = json.loads(fetch.content)

        headers = ["Service", "Estimate", "Price"]
        title = "Showing pricelist for shipping \nFrom: {} ({}) \nTo: {} ({}).\n".format(
            data['price'][0]['origin_name'], city_from,
            data['price'][0]['destination_name'], city_to)

        stack = []
        for entry in data['price']:
            times = entry.get('times', 'D')
            if times == 'H':
                est = "{} hour(s) - {} hours"
            else:
                est = "Over {} days - {} days"
            est = est.format(entry.get('etd_from'), entry.get('etd_thru'))

            stack.append(list((
                entry['service_display'],
                est,
                "IDR {}".format(entry.get('price', 0))
            )))

        print title
        print tabulate(stack, headers)
    else:
        print "JNE server is malformed."


def tracking(airwaybill):

    payload = USERKEY
    endpoint = URL_TRACKING % airwaybill
    useragent = random.choice(user_agent)

    fetch = requests.post(endpoint, data=payload, headers={
        'User-Agent': useragent
    })

    if fetch.status_code == 200:

        data = json.loads(fetch.content)

        detail = data.get("detail")[0]
        runsheet = data.get("runsheet")
        delivery = data.get("cnote")

        header_dtl = ["Package Detail", "", ""]
        stack_dtl = [

            ["Shipping Date", ":", detail.get('cnote_date')],
            ["Tracking Number", ":", detail.get("cnote_no")],
            [" ", " ", " "],
            ["Origin", ":", detail.get("cnote_origin")],
            ["Destination", ":", detail.get("cnote_destination")],
            [" ", " ", " "],
            ["Shipper Name", ":", detail.get("cnote_shipper_name")],
            ["Shipper Address", ":", "{}, {}, {}, {}".format(
                detail.get("cnote_shipper_addr1"),
                detail.get("cnote_shipper_addr2", "") or "-",
                detail.get("cnote_shipper_addr3"),
                detail.get("cnote_shipper_city"),
            )],
            [" ", " ", " "],
            ["Recipient Name", ":", detail.get("cnote_receiver_name")],
            ["Recipient Address", ":", "{}, {}, {}, {}".format(
                detail.get("cnote_receiver_addr1"),
                detail.get("cnote_receiver_addr2", "") or "-",
                detail.get("cnote_receiver_addr3"),
                detail.get("cnote_receiver_city"),
            )],
            [" ", " ", " "],
            ["Weight", ":", "{} Kg".format(detail.get("cnote_weight", 0))]
        ]


        header_rst = ['Transit', "Detail"]
        stack_rst = []
        for item in runsheet:
            stack_rst.append([
                item.get("city_name", ""),
                "{} - {}".format(item.get("mrsheet_date", 0), item.get("pod_status", ""))])


        header_dlv = ['Delivery', "", "Detail"]
        stack_dlv= [
            ["Delivered on", ":", delivery.get("cnote_pod_date")],
            ["Delivered at", ":", delivery.get("city_name")],
            ["Recipient", ":", delivery.get("cnote_receiver_name")],
            ["Receiver", ":", delivery.get("cnote_pod_receiver")],
            ["Service", ":", delivery.get("cnote_services_code")],
            ["Status", ":", delivery.get("pod_status")],

        ]

        print tabulate(stack_dtl, header_dtl)
        print """\n```````````````````\n"""
        print tabulate(stack_rst, header_rst)
        print """\n```````````````````\n"""
        print tabulate(stack_dlv, header_dlv)

    else:
        print "JNE server is malformed."
