# Smart File Auto-Namer

A backend utility script demonstrating dynamic string formatting using system runtime clock metrics.

## Engineering Overview
- **Time Extraction:** Utilizes `datetime.now()` parsing to capture mutable system states.
- **String Tokenization:** Employs `.strftime()` formatting configurations to eliminate illegal file naming characters (like `:` or `/`).
- **Path Merging:** Integrates `os.path.join` for secure destination mapping.

## Author Tashwill ,   2026 
