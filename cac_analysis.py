import matplotlib.pyplot as plt
import numpy as np

# Data
quarters = ['Q1', 'Q2', 'Q3', 'Q4']
cac = [225.99, 229.88, 230.14, 236.67]
average_cac = np.mean(cac)
industry_target = 150

# Create the plot
plt.figure(figsize=(10, 6))
bars = plt.bar(quarters, cac, color='skyblue', label='Quarterly CAC')
plt.axhline(y=industry_target, color='r', linestyle='--', label=f'Industry Target ({industry_target})')
plt.axhline(y=average_cac, color='g', linestyle='-', label=f'Average CAC ({average_cac:.2f})')


# Add labels and title
plt.xlabel('Quarter')
plt.ylabel('Customer Acquisition Cost (USD)')
plt.title('Quarterly Customer Acquisition Cost (CAC) vs. Industry Target')
plt.legend()

# Add value labels on top of the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval, f'{yval:.2f}', va='bottom', ha='center')


# Save the plot
plt.savefig('cac_trend.png')

print("Data analysis complete. Visualization saved as 'cac_trend.png'")
