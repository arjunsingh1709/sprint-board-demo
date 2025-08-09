import matplotlib.pyplot as plt

days = list(range(1, 11))
ideal = [40 - (i * 4) for i in range(10)]
actual = [40, 36, 36, 32, 27, 24, 18, 11, 7, 0]  # Example of actual progress

plt.figure(figsize=(8, 5))
plt.plot(days, ideal, 'g--', label='Ideal')
plt.plot(days, actual, 'b-o', label='Actual')
plt.xlabel('Day')
plt.ylabel('Story Points Remaining')
plt.title('Sprint Burndown Chart')
plt.legend()
plt.xticks(days)
plt.grid(True)
plt.savefig('burndown_chart.png')
plt.show()
