# Fubon Guardians 2026 Ticket Snapshot ⚾

This repository provides a static visual snapshot of the available seating for the **Fubon Guardians 2026 Season** after the exclusive priority booking period for **Arthur Legend** and **Arthur King** members.

## Project Overview
The goal of this project is to allow fans to quickly check the remaining ticket quantities across all 27 home games before the general public sale begins. 

- **Data Cut-off:** 2026/03/19 18:00 (Post-Member Priority Sale)
- **Source:** [FamiTicket Official Website](https://guardians.fami.life/UTK0204_)

## File Structure
- `index.html`: The main portal page. It uses a JavaScript-driven grid to organize and link all 27 game sessions with their respective themes/events.
- `[Date].html`: Static HTML snapshots for each game date (e.g., `0403.html`). These pages display the remaining seats per section.
- `[Date]_files/`: Supporting assets (CSS, JS, Images) required to render the seating charts correctly.
- `start.py`: A utility script used for data privacy and de-identification.

## Data Privacy & Scripts
### `start.py`
Since saving web pages locally often includes personal session data (such as ID numbers or member names) within the source code, this Python script was developed to:
1. Scan all `.html` files in the directory.
2. Search for sensitive personal identification strings.
3. Batch-replace them with a placeholder (`REDACTED`) to ensure user privacy before deployment.

## Disclaimer
- This is a **static snapshot** and does not reflect real-time ticket availability.
- For actual ticket purchases and live updates, please visit the official FamiTicket system.
- Detailed seat selection (specific seat numbers) is not available in these snapshots due to the nature of static HTML.

## Community Feedback
After sharing this tool on Threads, it received significant positive engagement from the Fubon Guardians fan community. Many fans expressed that the visual snapshot helped them coordinate their ticket-buying strategy more effectively.

You can check it on (in Chinese): [Link](https://www.threads.com/@gpna_1229/post/DWEB3oakabS)

---
*Developed for the Fubon Guardians Fan Community.*
