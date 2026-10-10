import numpy as np
import matplotlib.pyplot as plt

# Player Names
players = np.array([
    "MS Dhoni",
    "Virat Kohli",
    "Rohit Sharma",
    "Suresh Raina",
    "Ravindra Jadeja",
    "Shikhar Dhawan"
])
# Runs
runs = np.array([10773, 13906, 11168, 5615, 2756, 6793])
# Batting Average
average = np.array([50.6, 58.2, 49.0, 35.3, 32.5, 44.1])
# Hundreds
hundreds = np.array([10, 50, 32, 5, 0, 17])
print("===== Cricket Performance Analysis =====\n")
print("Players:")
print(players)
print("\nRuns:")
print(runs)
print("\nTotal Runs:", np.sum(runs))
print("Average Runs:", np.mean(runs))
print("Highest Runs:", np.max(runs))
print("Lowest Runs:", np.min(runs))
print("Median Runs:", np.median(runs))

# Highest run scorer
index = np.argmax(runs)
print("\nHighest Run Scorer:", players[index])
index=np.argmax(hundreds)
print("most hundreds by:",players[index])

# # --------------------
# # BAR CHART
# # --------------------

plt.figure(figsize=(8,5))
plt.bar(players, runs)

plt.title("Runs Scored by Cricketers")
plt.xlabel("Players")
plt.ylabel("Runs")
plt.xticks(rotation=20)

plt.show()

# # --------------------
# # PIE CHART
# # --------------------

plt.figure(figsize=(7,7))
plt.pie(runs, labels=players, autopct="%1.1f%%")

plt.title("Runs Contribution")
plt.show()

# # # --------------------
# # # LINE CHART
# # # --------------------

plt.figure(figsize=(8,5))
plt.plot(players, average, marker="o")

plt.title("Batting Average")
plt.xlabel("Players")
plt.ylabel("Average")
plt.xticks(rotation=20)

plt.show()

# # # --------------------
# # # HISTOGRAM
# # # --------------------

plt.figure(figsize=(8,5))
plt.hist(runs, bins=5)

plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.ylabel("Frequency")

plt.show()
