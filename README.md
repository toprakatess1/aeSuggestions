## Installation

Follow these steps to get the bot running on your local machine:

### Prerequisites

- Python 3.8 or higher installed. Download it from [python.org](https://www.python.org/downloads/).
- Git installed. Download from [git-scm.com](https://git-scm.com/downloads).

### Clone the Repository

```bash
git clone https://github.com/toprakatess1/aeSuggestion.git
cd aeSuggestion
```

### Set Up a Virtual Environment (Recommended)
Creating a virtual environment helps keep dependencies isolated


# Windows
```bash
python -m venv venv
venv\Scripts\activate
```

# macOS / Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Configure
Open the .env file and replace "your-token-here"
with your bot token.
And open the bot.py file with an editor and add your suggestion
channel id. You can find it in Line 16, just replace it with "channelid"

### Run the Bot
start the bot using
```bash
python bot.py
```