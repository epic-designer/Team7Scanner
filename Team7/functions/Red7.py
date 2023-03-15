""" © Team7 || RiZoeL """

from core import assistant
import asyncio 

async def passcmd_to_red(user, bancode, proof):
   if user.username:
      scan_message = f"/scan @{user.username} {bancode} {proof}"
   else:
      scan_message = f"/scan {user.id} {bancode} {proof}"
   await assistant.send_message("Red7Systembot", scan_message)
