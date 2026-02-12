# Page monitor

A lightweight Python utility designed to monitor websites, public Google Sheets, and online files for changes using MD5 content hashing and intelligent HTML filtering.

## Overview
This script polls a target URL at a defined interval. It distinguishes between raw data (like CSVs or PDFs) and web pages. For web pages, it utilizes **BeautifulSoup4** to strip away dynamic noise (scripts, styles, navs), ensuring alerts only trigger for actual content updates.

## Features
* **Smart Content Filtering:** Ignores `<script>`, `<style>`, and `<nav>` tags to prevent false positives on dynamic sites.
* **Universal Compatibility:** Works with Google Sheets (Published to Web), standard HTML, and direct file links.
* **Audio Alerts:** Triggers a system "buzzer" upon detecting a change.
* **Stealth Headers:** Uses browser-mimicking User-Agents to avoid being flagged as a bot.

## Prerequisites
* Python 3.x
* Required Libraries:
    ```bash
    pip install requests beautifulsoup4
    ```

## Configuration
1.  **URL Setup:** Replace the `URL` variable in the script with your target link.
2.  **Interval:** Adjust `INTERVAL` (default is 60 seconds).

## Usage
### Running Locally
```bash
python page-watch.py
```
## DISCLAIMER
This tool is intended for personal use. Users should ensure their polling frequency is "polite" (default 60s) to avoid putting unnecessary load on servers or violating the target's Terms of Service. The author is not responsible for misuse or unintended consequences of automation.
