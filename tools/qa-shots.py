# -*- coding: utf-8 -*-
"""V7-19 QA 截图协议：headless Chrome + force-prefers-reduced-motion 冻结入场动画。
用法: python tools/qa-shots.py <outdir> <round-tag>
拍 5 个代表页 x 桌面1440x900 / 手机390x844，存 <outdir>/。"""
import subprocess, os, sys, time

CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
BASE = "http://127.0.0.1:8765"
PAGES = ["index", "reading", "timeline", "companies", "search"]
VIEWPORTS = [("desktop", 1440, 900), ("mobile", 390, 844)]

def main():
    outdir = sys.argv[1] if len(sys.argv) > 1 else "qa/v7-19/round-01/before"
    os.makedirs(outdir, exist_ok=True)
    for tag, w, h in VIEWPORTS:
        for p in PAGES:
            out = os.path.abspath(os.path.join(outdir, f"{p}-{tag}.png"))
            cmd = [
                CHROME, "--headless=new", "--disable-gpu",
                "--force-prefers-reduced-motion",
                "--hide-scrollbars", "--disable-extensions",
                "--virtual-time-budget=6000",
                f"--window-size={w},{h}",
                f"--screenshot={out}",
                f"{BASE}/{p}.html",
            ]
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            ok = os.path.exists(out) and os.path.getsize(out) > 10000
            print(("OK  " if ok else "FAIL") + f" {p}-{tag}.png {os.path.getsize(out) if os.path.exists(out) else 0}B")
            if not ok:
                print("  stderr:", (r.stderr or "")[-300:])
    print("done")

if __name__ == "__main__":
    main()
