# AI-Based Phishing Detection Framework
## Feature Schema

This document defines the features extracted from every URL.

The same feature extraction logic is used for:

- Dataset Generation
- Model Training
- Flask Prediction API

This ensures consistency between training and inference.

---

## Feature List

| No | Feature Name | Data Type | Description |
|----|--------------|-----------|-------------|
| 1 | URL_Length | Integer | Total length of the URL |
| 2 | Domain_Length | Integer | Length of domain name |
| 3 | Path_Length | Integer | Length of URL path |
| 4 | Query_Length | Integer | Length of query string |
| 5 | Num_Dots | Integer | Number of '.' characters |
| 6 | Num_Hyphens | Integer | Number of '-' characters |
| 7 | Num_Underscores | Integer | Number of '_' characters |
| 8 | Num_Slashes | Integer | Number of '/' characters |
| 9 | Num_Digits | Integer | Total digits in URL |
|10 | Num_Special_Chars | Integer | Number of special characters |
|11 | Num_Subdomains | Integer | Number of subdomains |
|12 | Has_IP | Boolean | Domain is IP address |
|13 | Has_HTTPS | Boolean | Uses HTTPS |
|14 | Has_At_Symbol | Boolean | '@' present |
|15 | Has_Prefix_Suffix | Boolean | Hyphen in domain |
|16 | Has_Redirection | Boolean | Extra '//' after protocol |
|17 | Tiny_URL | Boolean | URL shortener used |
|18 | Suspicious_Keyword_Count | Integer | Number of phishing keywords |
|19 | Contains_Login | Boolean | Contains 'login' |
|20 | Contains_Verify | Boolean | Contains 'verify' |
|21 | Contains_Update | Boolean | Contains 'update' |
|22 | Contains_Bank | Boolean | Contains 'bank' |
|23 | Contains_Secure | Boolean | Contains 'secure' |
|24 | Entropy | Float | URL randomness score (optional) |
|25 | Label | Integer | 0 = Legitimate, 1 = Phishing |

---

## Feature Categories

### URL Structure
- URL_Length
- Domain_Length
- Path_Length
- Query_Length

### Character Statistics
- Num_Dots
- Num_Hyphens
- Num_Underscores
- Num_Slashes
- Num_Digits
- Num_Special_Chars

### Domain Features
- Num_Subdomains
- Has_IP
- Has_Prefix_Suffix

### Security Features
- Has_HTTPS
- Has_At_Symbol
- Has_Redirection

### URL Shortener
- Tiny_URL

### Suspicious Content
- Suspicious_Keyword_Count
- Contains_Login
- Contains_Verify
- Contains_Update
- Contains_Bank
- Contains_Secure

### Advanced
- Entropy

---

## Target Variable

0 → Legitimate Website

1 → Phishing Website