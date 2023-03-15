import re

async def check_reason(message, reason):
  if re.search("T7x00".lower(), reason.lower()):
     return "T7x00 - Scammer", "R7x00"
  elif re.search("T7x01".lower(), reason.lower()):
     return "T7x01 - Mass Adding Member", "R7x01"
  elif re.search("T7x02".lower(), reason.lower()):
     return "T7x02 - Child Abuse", "R7x02"
  elif re.search("T7x03".lower(), reason.lower()):
     return "T7x03 - Illegal", "R7x03"
  elif re.search("T7x04".lower(), reason.lower()):
     return "T7x04 - Fraud Promotion", "R7x04"
  elif re.search("T7x05".lower(), reason.lower()):
     return "T7x05 - Phishing", "R7x05"
  elif re.search("T7x06".lower(), reason.lower()):
     return "T7x06 - Ban Evasion", "R7x06"
  elif re.search("T7x07".lower(), reason.lower()):
     return "T7x07 - Raid/spam Inflamed", "R7x07"
  elif re.search("T7x08".lower(), reason.lower()):
     return "T7x08 - Adding Spambots/raiders", "R7x08"
  elif re.search("T7x09".lower(), reason.lower()):
     return "T7x09 - Kriminalant", "R7x09"
  elif re.search("T7x10".lower(), reason.lower()):
     return "T7x10 - Fake/Scammer", "R7x10"
  elif re.search("T7x11".lower(), reason.lower()):
     return "T7x11 - Abuse Spam", "R7x11"
  elif re.search("T7x12".lower(), reason.lower()):
     return "T7x12 - Impersonation", "R7x12"
  elif re.search("T7x13".lower(), reason.lower()):
     return "T7x13 - Md/btc Scam", "R7x13"
  elif re.search("T7x14".lower(), reason.lower()):
     return "T7x14 - Raid Initializer", "R7x14"
  elif re.search("T7x15".lower(), reason.lower()):
     return "T7x15 - Raid Participant", "R7x15"
  elif re.search("T7x16".lower(), reason.lower()):
     return "T7x16 - Spambots", "R7x16"
  elif re.search("T7x17".lower(), reason.lower()):
     return "T7x17 - Cyber Threatening/Bully", "R7x17"
  elif re.search("T7x18".lower(), reason.lower()):
     return "T7x18 - NSFW Spammer", "R7x18"
  else:
     return "Null", "Null"


Bancodestext = """
**Team7 Reason/Bancodes!**
 • {`T7x00`} - Scammer
 • {`T7x01`} - Mass Adding Member
 • {`T7x02`} - Child Abuse
 • {`T7x03`} - Illegal
 • {`T7x04`} - Fraud Promotion (Any Kind)
 • {`T7x05`} - Phishing
 • {`T7x06`} - Ban Evasion
 • {`T7x07`} - Raid/spam Inflamed
 • {`T7x08`} - Adding Spambots/raiders
 • {`T7x09`} - Kriminalant
 • {`T7x10`} - Fake/Scammer
 • {`T7x11`} - Abuse Spam
 • {`T7x12`} - Impersonation
 • {`T7x13`} - Md/btc Scam
 • {`T7x14`} - Raid Initializer
 • {`T7x15`} - Raid Participant
 • {`T7x16`} - Spambots
 • {`T7x17`} - Cyber Threatening/Bully
 • {`T7x18`} - NSFW Spammer
"""

