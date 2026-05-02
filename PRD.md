# PRD: sgAveroTech2021

## Overview
A Python + JavaScript toolkit for scraping student profile photos from Singapore school portals using the Avero Technology student management system. The MD5-based portal authentication was reverse-engineered from the portal's JavaScript login flow. Active until approximately June 2021 when the target systems were updated. Built for educational security research.

## Goals
- Authenticate to Avero Tech school portals via MD5-hashed credentials
- Scrape and download student profile photos
- Generate MD5 hashes for portal authentication tokens
- Enumerate student IDs to discover photo endpoints

## Non-Goals
- Accessing private student records beyond photos
- Production use or automation at scale
- Any use against systems you don't have authorization to test

## Tech Stack
- **Language**: Python 3.x, JavaScript (Node.js for MD5 generation)
- **Libraries**: `requests`, `BeautifulSoup` (implied), `hashlib`
- **Files**: `getimages.py`, `loginforportal.js`, `md5forportal.js`, `md5generate.py`

## Architecture
```
sgAveroTech2021/
├── getimages.py              # Downloads profile photos
├── loginforportal.js         # JavaScript login flow (reverse-engineered)
├── md5forportal.js           # MD5 hash generation matching portal auth
├── md5generate.py            # Python MD5 generation
├── randomidsinportal.txt     # Sample student IDs found in portal
└── samplemd5s.txt            # Sample MD5 hashes
```

## Deployment / Run
```bash
pip install requests beautifulsoup4
python getimages.py
```

## Constraints & Notes
- **INACTIVE**: school portals updated in June 2021 — authentication flow no longer works
- **Legal/Ethical**: scraping student photos from school portals without authorization violates PDPA (Singapore Personal Data Protection Act) and likely the school's computer use policies. This code is preserved as a historical security research artifact only.
- **MD5 auth**: portal used MD5-hashed credentials with static salt — a known-weak authentication pattern, now patched
- **Educational value**: demonstrates reverse engineering of a weak authentication flow
