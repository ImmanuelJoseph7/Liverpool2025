import pandas as pd
import matplotlib.pyplot as plt

# Load the data directly from GitHub
matches_url = r"C:\External Git Repos\Club-Football-Match-Data-2000-2025\data\Matches.csv"
elo_url = r"C:\External Git Repos\Club-Football-Match-Data-2000-2025\data\EloRatings.csv"

# Read the CSV files
matches_df = pd.read_csv(matches_url, low_memory=False)
elo_df = pd.read_csv(elo_url)

print(matches_df.columns)


# Filter Liverpool matches from 2015 to 2025
liverpool_matches = matches_df[
    ((matches_df['HomeTeam'] == 'Liverpool') | (matches_df['AwayTeam'] == 'Liverpool')) &
    (matches_df['MatchDate'].str[:4].astype(int).between(2005, 2025))
]

# Preview the data
liverpool_matches.to_csv('liverpool_matches_2015_2025.csv', index=False)

# Filter Elo ratings for Liverpool and Manchester United
liverpool_elo = elo_df[
    (elo_df['club'] == 'Liverpool') &
    (elo_df['date'].str[:4].astype(int).between(2005, 2025))
].copy()

manutd_elo = elo_df[
    (elo_df['club'] == 'Arsenal') &
    (elo_df['date'].str[:4].astype(int).between(2005, 2025))
].copy()

# Convert 'date' to datetime for plotting
liverpool_elo['date'] = pd.to_datetime(liverpool_elo['date'])
manutd_elo['date'] = pd.to_datetime(manutd_elo['date'])

# Preview Elo ratings
print(liverpool_elo[['date', 'elo']].head())
liverpool_elo.to_csv('liverpool_elo_2015_2025.csv', index=False)
manutd_elo.to_csv('manutd_elo_2015_2025.csv', index=False)
# Plot Elo ratings over time for both teams
plt.figure(figsize=(12, 6))
plt.plot(liverpool_elo['date'], liverpool_elo['elo'], marker='o', label='Liverpool')
plt.plot(manutd_elo['date'], manutd_elo['elo'], marker='x', label='Manchester United')
plt.title('Elo Ratings: Liverpool vs Manchester United (2005-2025)')
plt.xlabel('Date')
plt.ylabel('Elo Rating')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()