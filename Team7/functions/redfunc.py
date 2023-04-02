""" © Team7 || RiZoeL """

from Team7.core import assistant
import asyncio 

async def passcmd_to_red(user, bancode, proof):
   if user.username:
      scan_message = f"/scan @{user.username} {bancode} {proof}"
   else:
      scan_message = f"/scan {user.id} {bancode} {proof}"
   await assistant.send_message("Red7Systembot", scan_message)

async def revert_to_red(user):
   if user.username:
      revert_message = f"/revert @{user.username}"
   else:
      revert_message = f"/revert {user.id}"
   await assistant.send_message("Red7Systembot", revert_message)

