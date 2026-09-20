"""
BloodStrike Offset Dumper
By RKmodz / mr__zerooo — v2.0
"""

import os
import re
import sys
import struct
import ctypes
import ctypes.wintypes as wt
import time
import traceback
from datetime import datetime

# ============================================================
# Console Colors (ANSI)
# ============================================================
class C:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    DIM     = "\033[2m"

    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    GRAY    = "\033[90m"

    BG_RED    = "\033[41m"
    BG_GREEN  = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE   = "\033[44m"
    BG_CYAN   = "\033[46m"

def enable_ansi():
    """Enable ANSI escape codes on Windows."""
    kernel32 = ctypes.windll.kernel32
    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)

def slow_print(text, delay=0.01):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner():
    art = f"""{C.CYAN}{C.BOLD}
  ╔══════════════════════════════════════════════════════════╗
  ║                                                          ║
  ║        B L O O D S T R I K E   D U M P E R              ║
  ║           v2.0  ·  Offset Scanner & SDK Generator        ║
  ║                                          by mr__zerooo   ║
  ╚══════════════════════════════════════════════════════════╝{C.RESET}
"""
    print(art)

def section_header(step, title):
    label = f"  [{step}]  {title}"
    print(f"\n{C.CYAN}{C.BOLD}{label}{C.RESET}")
    print(f"  {C.GRAY}{'─' * (len(label) - 2)}{C.RESET}")

def status(msg, color=None):
    c = color or C.WHITE
    print(f"    {c}→  {msg}{C.RESET}")

def progress_bar(current, total, width=30, label=""):
    pct = current / total
    filled = int(width * pct)
    bar = f"{C.GREEN}{'█' * filled}{C.GRAY}{'░' * (width - filled)}{C.RESET}"
    pct_str = f"{C.YELLOW}{pct * 100:5.1f}%{C.RESET}"
    sys.stdout.write(f"\r    {bar} {pct_str}  {C.DIM}{label}{C.RESET}")
    sys.stdout.flush()
    if current == total:
        print()
