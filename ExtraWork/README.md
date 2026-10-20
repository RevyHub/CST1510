# Extra Work

The exercises are separated by teaching week in `weeks/`. Run one week
directly with Python, for example:

```powershell
python .\weeks\week_01.py
```

| File | Main topics |
| --- | --- |
| `week_01.py` | Input, output, arithmetic, conversions, and simple reports |
| `week_02.py` | Conditions, loops, random numbers, and small games |
| `week_03.py` | Functions, lambdas, unit conversion, and string exercises |
| `week_04.py` | Lists, dictionaries, sets, statistics, and CSV parsing |
| `week_05.py` | Classes, objects, and basic account/course models |
| `week_06.py` | Pandas data analysis, grouping, and missing values |
| `week_07.py` | Word counts, ciphers, text cleaning, and search |
| `week_08.py` | HTTP requests, regular expressions, and IP parsing |
| `week_09.py` | Password hashing and file-based registration/login |
| `week_10.py` | SQLite, parameterized queries, and CSV import/export |
| `week_11.py` | Streamlit login and student dashboard examples |
| `week_12.py` | OpenAI chat examples |

The original `extra projects.py` is a legacy combined copy. Use the files in
`weeks/` so running one week's exercises does not start every earlier task.

## Setup

Install the packages used by the later weeks from the coursework folder:

```powershell
python -m pip install -r .\ExtraWork\requirements.txt
```

Weeks 4, 6, 10, and 11 use CSV files in `DATA/`. Week 7's file-based
word-count example also accepts an optional `Les_Brown.txt` in that folder.
Weeks 11 and 12 share a working multipage Streamlit app. Start it from the
CST1510 folder with:

```powershell
python -m streamlit run .\ExtraWork\streamlit_app\Home.py
```

The demo login is `alice` / `admin123` or `bob` / `user123`.
These hard-coded accounts are for coursework demonstrations only, not real
authentication.

Week 12's console and Streamlit AI examples require an `OPENAI_API_KEY`
environment variable and may incur API charges. Do not put API keys in source
code or commit them.