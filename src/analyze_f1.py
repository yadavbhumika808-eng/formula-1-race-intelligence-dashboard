from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
WORKBOOK = ROOT / "data" / "F1_Racing_Project_Dataset.xlsx"
OUT = ROOT / "outputs"

def main():
    OUT.mkdir(exist_ok=True)
    xls = pd.ExcelFile(WORKBOOK)
    print("Workbook:", WORKBOOK.name)
    for sheet in xls.sheet_names:
        df = pd.read_excel(WORKBOOK, sheet_name=sheet)
        print(f"{sheet}: {len(df):,} rows x {len(df.columns)} columns")
        pd.DataFrame({
            "column": df.columns,
            "dtype": [str(df[c].dtype) for c in df.columns],
            "missing_count": [int(df[c].isna().sum()) for c in df.columns],
            "missing_pct": [round(float(df[c].isna().mean() * 100), 2) for c in df.columns],
        }).to_csv(OUT / f"{sheet}_data_quality.csv", index=False)

    races = pd.read_excel(WORKBOOK, sheet_name="race_results")
    if "season" in races:
        print("Race-results season range:", races["season"].min(), "-", races["season"].max())
        races.groupby("season", dropna=False).agg(
            rows=("season", "size"),
            unique_races=("race_id", "nunique") if "race_id" in races else ("season", "size"),
            drivers=("driver", "nunique") if "driver" in races else ("season", "size"),
            teams=("team", "nunique") if "team" in races else ("season", "size"),
        ).reset_index().to_csv(OUT / "season_summary.csv", index=False)

    print(f"Data quality summaries saved to: {OUT}")

if __name__ == "__main__":
    main()
