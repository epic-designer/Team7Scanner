""" Team7 || RiZoeL """

import os, sys, asyncio, psutil, cpuinfo, platform
from .version import __version__
from .config import Channel, Support 

from pyrogram import __version__ as pyro_vr
from pyRiZoeLX import __version__ as rizoelx_vr

from Team7.database import users_db, scan_db, report_db

from pyrogram.types import InlineKeyboardButton


def get_stats():
    stats_msg = "**------ Team7 - Scanner ------**\n"
    try:
        diskTotal = int(psutil.disk_usage('/').total / (1024 * 1024 * 1024))
        diskUsed = int(psutil.disk_usage('/').used / (1024 * 1024 * 1024))
        diskPercent = psutil.disk_usage('/').percent
        disk = f"{diskUsed}GB / {diskTotal}GB ({diskPercent}%)"
    except:
        disk = "Unknown"
    stats_msg += f"**Disk:** {disk} \n"

    try:
        ramTotal = int(psutil.virtual_memory().total / (1024 * 1024))
        ramUsage = int(psutil.virtual_memory().used / (1024 * 1024))
        ramUsagePercent = psutil.virtual_memory().percent
        ram = f"{ramUsage}MB / {ramTotal} MB ({ramUsagePercent}%)"
    except:
        ram = "Unknown"
    stats_msg += f"**Ram:** {ram} \n"

    try:
        cpuInfo = cpuinfo.get_cpu_info()['brand_raw']
        cpuUsage = psutil.cpu_percent(interval=1)
        cpu = f"{cpuInfo} ({cpuUsage}%)"
    except:
        cpu = "Unknown"
    stats_msg += f"**CPU:** {cpu} \n"

    try:
        os = f"{platform.system()} - {platform.release()} ({platform.machine()})"
    except:
        os = "Unknown"
    stats_msg += f"**OS:** {os} \n"
    
    try:
        battery = f"{int(psutil.sensors_battery().percent)}%"
    except:
        battery = f"Unknown"
    stats_msg += f"**Battery:** {battery} \n\n"

    stats_msg += f"  **• Total Devs:** `{users_db.dev_count()}` \n"
    stats_msg += f"  **• Total Red-Sudo:** `{users_db.sudo_count()}` \n"
    stats_msg += f"  **• Total Bots:** `{users_db.bot_count()}` \n\n"
    stats_msg += f"  **• Total scanned users:** `{scan_db.scan_count()}` \n"
    stats_msg += f"  **• Total reported users:** `{report_db.report_count()}` \n"
    stats_msg += "------ © Team7 || RiZoeL ------"
    return stats_msg

alive_msg = f"""
** × Team7 Scanner Here × ***

 • **Team7-scanner Ver:** `{__version}`
 • **Python ver:** `{platform.python_version()}`
 • **pyrogram ver:** `{pyro_vr}`
 • **pyRiZoeLX ver:** `{rizoelx_vr}`
"""

start_msg = """
**Hey {}!** I'm Team7's Scanner! Ab advance and powerful pyrogram based scanner!

**INFO:** Team7-scanner is simple scanner! if you want to join Team7Scanner just give sudo to assistant and take approval from devs!
"""

alive_buttons = [
                [
                 InlineKeyboardButton(
                      "• Channel ", url=f"https://t.me/{Channel}"),
                 InlineKeyboardButton(
                      " Support •", url=f"https://t.me/{Support}")
                ],
                ]

start_buttons = [
                [
                 InlineKeyboardButton(
                      "• Channel ", url=f"https://t.me/{Channel}"),
                 InlineKeyboardButton(
                      " Support •", url=f"https://t.me/{Support}")
                ], [
                 InlineKeyboardButton(
                      "Report User", callback_data="do_report")
                ],
                ]

stats_buttons = [
                [
                 InlineKeyboardButton(
                      "× Alive", callback_data="alive"),
                 InlineKeyboardButton(
                      "Ping ×", callback_data="ping")
                ],
                ]




