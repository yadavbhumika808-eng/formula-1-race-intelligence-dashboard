# Formula 1 Race Intelligence Dashboard Analysis Report (2010–2026)

An exploratory data analytics project using Formula 1 race, qualifying, championship, circuit, and lap-intelligence data. The project is designed for analysis in Tableau, with Python/Pandas available for validation and exploratory analysis.

## Project objectives
- Compare driver and constructor championship performance across seasons.
- Explore race finishes, grid positions, positions gained, and DNF patterns.
- Investigate qualifying pace, gaps to pole, and sector performance.
- Explore lap times, tyre compounds, tyre age, DRS, speed-trap readings, and pit-lap indicators where available.
- Compare circuit characteristics and race conditions.

## Dataset
The provided workbook is `data/F1_Racing_Project_Dataset.xlsx`. It contains five sheets:

| Sheet | Rows | Purpose |
|---|---:|---|
| `circuits` | 29 | Circuit metadata: country, city, length, type, altitude and direction |
| `championship_standings` | 311 | Driver standings, points, wins, podiums, poles, DNFs and champion flag |
| `lap_intelligence` | 3,814 | Lap-level timing, sectors, tyre compound/age, DRS and speed-trap values |
| `qualifying_results` | 3,130 | Qualifying position, lap times, sector times and gap to pole |
| `race_results` | 6,464 | Race result, grid, points, DNF, weather, pit stops, tyre strategy and overtakes |

**Data-quality note:** This workbook is the dataset supplied for this project. Validate its values and provenance before presenting conclusions as official historical F1 statistics. The season range in the title does not by itself prove that every record is official or complete. Treat missing values as missing, not zero, and document any data limitations.

## Tools
- Microsoft Excel — workbook inspection
- Python 3.10+ and Pandas — optional data validation / summary generation
- Tableau Desktop or Tableau Public — charts, dashboard and story
- GitHub — version control and project documentation

## Suggested Tableau worksheets
1. Driver Wins by Season
2. Driver Points Trend
3. Constructor Performance
4. Circuit Overview
5. Qualifying Position vs Race Finish
6. DNF and Reliability Analysis
7. Pole Position vs Race Wins
8. Lap Pace and Sector Analysis
9. Tyre Strategy / Pit Stop Analysis

## Dashboard plan
**Title:** Formula 1 Race Intelligence Dashboard (2010–2026)

Suggested filters: Season, Driver, Constructor, Circuit Country, Circuit Type, Weather, DNF Reason, Tyre Compound.

Suggested KPI cards: Seasons covered, races represented, unique drivers, constructors, circuits, DNF count.

## Data relationships and grain
- `race_results` ↔ `circuits`: `circuit_id`
- `race_results` ↔ `qualifying_results`: use both `race_id` and `driver` when matching driver-race records
- `race_results` ↔ `lap_intelligence`: use both `race_id` and `driver` for driver-race comparisons
- `championship_standings` is season/driver-level data; relate by season and driver only when the intended grain is appropriate.

Avoid joining all sheets into one flat table without checking row duplication. Lap-level and race-level tables have different grains, so a careless join can multiply counts and points.

## Run optional Python data checks
```bash
pip install -r requirements.txt
python src/analyze_f1.py
```
The script reports workbook dimensions, missing values, season coverage, and basic summary CSVs in `outputs/`.

## Deliverables to add
- Tableau workbook (`.twb` or `.twbx`, subject to dataset licensing)
- Dashboard screenshot(s) in `screenshots/`
- A published Tableau Public demo URL, if appropriate
- A short findings section based on actual charts

## Limitations
This repository documents the analysis workflow. Do not claim that a Tableau dashboard is complete until the workbook and dashboard have actually been created and tested. Check dataset provenance/licensing before redistributing the data or publishing the workbook publicly.
