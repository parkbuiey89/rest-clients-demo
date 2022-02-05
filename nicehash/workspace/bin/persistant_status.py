#!/usr/bin/env python3

import requests
import nicehash
import json
import smtplib

class Rig_query:

    connection = None
    query_string = None
    stats_list = []
    rig_data = None

    def __init__(self):
        
        self.rig_data = '../lib/rig_results.txt'
        self.connection = self.rig_connect()
        self.write_to_list()
        self.write_to_file()
        self.decision_maker()



    def rig_connect(self):

        host = 'https://api2.nicehash.com'
        organisation_id = '72399a18-7a4a-49a4-bcc2-fc8d0aa45447'
        key = '2a941125-1a6d-45b2-93db-b2d05e905288'
        secret = 'aca95426-be53-4bd4-9767-30612a1fe6cc2b6d3f9b-7e33-4285-9243-1e57c8fa56f5'
        size = 25
        page = 0

        private_api = nicehash.private_api(host, organisation_id, key, secret)
        my_accounts = private_api.get_rig_stats(size, page)
        return my_accounts

    def write_to_list(self):

        results = self.connection
        for x in results['minerStatuses']:
            self.stats_list.append(x)

    def write_to_file(self):

        output = self.stats_list
        f = open(self.rig_data, 'w')
        f.write(str(output))
        f.close()
            
    def decision_maker(self):

        yes = self.stats_list
        if yes == ['OFFLINE']:
            self.send_mail()

    def send_mail(self):

        username = 'ian.nelson622@gmail.com'
        password = 'Facebook#1'
        Subject = "Rig Status"
        FromMy = "ian.nelson622@gmail.com"
        To = "ian.nelson62@yahoo.com"
        message_to_send = ''
        f = open('/home/joe/Desktop/python/nicehash/workspace/lib/rig_results.txt', 'r')
        for x in f:
            message_to_send += x
        msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % ( FromMy, To, Subject, message_to_send )
        b = smtplib.SMTP('smtp.gmail.com',587)
        b.ehlo()
        b.starttls()
        b.ehlo()
        b.login(username,password)
        b.sendmail(FromMy, To ,msg)
        b.quit()





r = Rig_query()

