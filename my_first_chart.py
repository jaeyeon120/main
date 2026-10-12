import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "AppleGothic"

temperatures = [25, 29, 27, 25, 26]

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(temperatures)
for i, p in enumerate(temperatures):
    ax.annotate(f"{p:,}", (i, p), textcoords="offset points",
                xytext=(0, 8), ha="center")

ax.set_title("5일 기온 변화")
fig.savefig("my_first_chart.png")