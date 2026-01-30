# Google Flights USD

A Chrome extension that automatically sets the currency to USD on Google Flights.

## Why?

Google Flights uses your IP address to determine your local currency, which can be inconvenient when traveling or using a VPN. This extension ensures prices are always displayed in USD.

## What It Does

When you visit any Google Flights URL, the extension automatically adds these parameters:
- `curr=usd` - Sets currency to US Dollars
- `hl=en` - Sets language to English
- `gl=us` - Sets region to United States

The redirect happens before the page loads using Chrome's `declarativeNetRequest` API, so there's no page flash or double-load.

## Installation

1. Clone this repository or download the files
2. Open Chrome and navigate to `chrome://extensions/`
3. Enable **Developer mode** (toggle in top-right corner)
4. Click **Load unpacked**
5. Select the folder containing the extension files

## Files

- `manifest.json` - Extension configuration (Manifest V3)
- `rules.json` - URL redirect rules
- `icons/` - Extension icons (16px, 48px, 128px)

## Permissions

- `declarativeNetRequest` - Required to modify URLs before page load
- Host permission for `www.google.com/travel/flights*` only

## License

MIT
