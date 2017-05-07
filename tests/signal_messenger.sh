#!/bin/bash

#prints version
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -v

#no visual feedback when this runs successfully
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 register
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 register

#Go to https://smsreceivefree.com
#Your Signal verification code: 627-717
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 verify 627-717
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 verify 632-271

#to view profile data
#cat /home/dneary/.config/signal/data/+15304548041

#register 2nd phone number: +14232050478
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 register

#verify with code received from smsreceivefree.com
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 verify 564-841

#send a message from 1st to 2nd
#signal-cli -u USERNAME send -m "This is a message" RECIPIENT
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 send -m "This is an SS message" +14232050478

#receive a message sent from 1st to 2nd number
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 receive
#reply text below
#Envelope from: +15304548041 (device: 1)
#Timestamp: 1494001645568 (2017-05-05T16:27:25.568Z)
#Message timestamp: 1494001645568 (2017-05-05T16:27:25.568Z)
#Body: This is a d message

#send a message from 2nd to 1st number
#signal-cli -u USERNAME send -m "This is a message" RECIPIENT
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 send -m "This is a 2 message" +15304548041

#receive message from 2nd to 1st
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 receive
#reply text below
##Envelope from: +14232050478 (device: 1)
#Timestamp: 1494001645568 (2017-05-05T16:27:25.568Z)
#Got receipt.

#Envelope from: +14232050478 (device: 1)
#Timestamp: 1494002546075 (2017-05-05T16:42:26.075Z)
#Message timestamp: 1494002546075 (2017-05-05T16:42:26.075Z)
#Body: This is a 2 message


/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 listIdentities

/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 listIdentities
#output from above commands, look at this
dneary@dell-m6700-laptop:~/Documents/vcs/git/zerophone$ /home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 listIdentities
+14232050478: TRUSTED_UNVERIFIED Added: Fri May 05 09:27:26 PDT 2017 Fingerprint: 05 38 7d 2f 8c b9 54 63 56 67 6a 9f fe d6 d7 8f 1a 8c b4 fb 42 54 6f c8 ed 86 62 48 93 71 d2 07 6a  Safety Number: 49732 18248 40470 57988 13494 14199 85394 48785 85187 78025 87194 88369 
+14232050478: UNTRUSTED Added: Sat May 06 12:42:18 PDT 2017 Fingerprint: 05 7c d6 3b 93 27 a4 7c 98 59 a9 4e 86 2c eb 84 f0 97 99 e8 f7 08 ab 9e c3 7a 87 d2 f4 a9 2c c5 3c  Safety Number: 85394 48785 85187 78025 87194 88369 95060 76588 94649 52552 10403 11577 
dneary@dell-m6700-laptop:~/Documents/vcs/git/zerophone$ /home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +14232050478 listIdentities
Authorization failed, was the number registered elsewhere?
+15304548041: TRUSTED_UNVERIFIED Added: Fri May 05 09:37:18 PDT 2017 Fingerprint: 05 fd 00 bc 78 b4 c8 4e 9f f2 92 23 7c cf 32 71 d3 a9 ac d5 d1 49 d3 7c f0 66 cd 27 bf 0d 40 a5 53  Safety Number: 49732 18248 40470 57988 13494 14199 85394 48785 85187 78025 87194 88369 

#right after creation
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 listIdentities
#returns nothing

#after sending 1st message
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +15304548041 send -m "This is an SSS message" +13513331152

/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 listIdentities
#still returns nothing

/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 receive
Envelope from: +15304548041 (device: 1)
Timestamp: 1494116676312 (2017-05-07T00:24:36.312Z)
Message timestamp: 1494116676312 (2017-05-07T00:24:36.312Z)
Body: This is an SSS message

#
/home/dneary/Downloads/2017/signal-cli-0.5.5/bin/signal-cli -u +13513331152 listIdentities
+15304548041: TRUSTED_UNVERIFIED Added: Sat May 06 17:30:17 PDT 2017 Fingerprint: 05 fd 00 bc 78 b4 c8 4e 9f f2 92 23 7c cf 32 71 d3 a9 ac d5 d1 49 d3 7c f0 66 cd 27 bf 0d 40 a5 53  Safety Number: 40013 57944 07818 40089 70682 41397 85394 48785 85187 78025 87194 88369 
